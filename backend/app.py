from flask import Flask, jsonify, request
from flask_cors import CORS
from extensions import db, security
from flask_security import SQLAlchemyUserDatastore, hash_password
from datetime import datetime
from flask import send_from_directory, abort, url_for
from models import User, Role, BlogPost, Application, Event, EventRegistration, Course, GalleryImage, ContactMessage, TeamMember
from resources.blog import blog_bp
from resources.events import events_bp
from resources.auth import auth_bp
from resources.team import team_bp
from resources.gallery import gallery_bp
from resources.uploads import uploads_bp
import os

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-yantra')
    app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yantra.db'
    app.config['SECURITY_PASSWORD_HASH'] = 'pbkdf2_sha512'
    app.config['SECURITY_PASSWORD_SALT'] = os.environ.get('SECRET_KEY', 'yantra-salt')
    app.config['SECURITY_REGISTERABLE'] = False
    app.config['SECURITY_SEND_REGISTER_EMAIL'] = False
    app.config['SECURITY_TOKEN_AUTHENTICATION_HEADER'] = 'Authorization'
    app.config['SECURITY_FLASH_MESSAGES'] = False
    
    # Initialize Extensions
    CORS(app)
    db.init_app(app)
    
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)
    
    # Register Blueprints
    app.register_blueprint(blog_bp, url_prefix='/api/blog')
    app.register_blueprint(events_bp, url_prefix='/api/events')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(team_bp, url_prefix='/api/team')
    app.register_blueprint(gallery_bp, url_prefix='/api/gallery')
    app.register_blueprint(uploads_bp, url_prefix='/api/uploads')

    @app.get('/api/uploads/<path:filename>')
    def uploaded_file(filename):
        from pathlib import Path
        upload_dir = Path(app.root_path) / 'uploads'
        if not (upload_dir / filename).is_file():
            abort(404)
        return send_from_directory(upload_dir, filename)

    @app.errorhandler(413)
    def request_too_large(_error):
        return jsonify({'error': 'Upload is too large. Maximum file size is 8 MB.'}), 413

    with app.app_context():
        db.create_all()

        # SQLite create_all does not add columns to tables that already exist.
        from sqlalchemy import inspect, text
        inspector = inspect(db.engine)
        for table, additions in {
            'events': {'image_url': 'VARCHAR(500)', 'registration_url': 'VARCHAR(500)', 'max_attendees': 'INTEGER'},
            'gallery': {'category': "VARCHAR(50) DEFAULT 'general'", 'sort_order': 'INTEGER DEFAULT 0'},
        }.items():
            existing = {column['name'] for column in inspector.get_columns(table)}
            for column, definition in additions.items():
                if column not in existing:
                    db.session.execute(text(f'ALTER TABLE {table} ADD COLUMN {column} {definition}'))
        db.session.commit()

        # Preserve the roster that was previously embedded in Team.vue.
        if TeamMember.query.count() == 0:
            roster = [
                ('Sayed Zainuddin', 'Session Host', 'Guides robotics sessions, keeps demos moving, and helps participants stay locked into the build.', 'Hosting,Workshops,Robotics', 'sessionhost.png'),
                ('Kaushik Harsha', 'Web Dev Lead', 'Leads web development and ensures the Yantra site stays polished, responsive, and performance-optimized.', 'Frontend/UX,Vue.js,Flask', 'webdev.png'),
                ('Harsh Rathee', 'Creative Team', 'Shapes Yantra’s creative identity through visuals, branding, and event design.', 'Design,Branding,Creative Direction', 'harshcreative.png'),
                ('Dheepika R', 'Creative (Poster Design)', 'Designs event posters, promotional graphics, and visual campaigns for Yantra events.', 'Poster Design,Graphic Design,Brand Collateral', 'dheepikacreative.jpeg'),
                ('Finny Varghese', 'Founding member of Yantra’s Administrative Council and Industry Mentor', 'Bringing professional robotics experience from the UK’s deep-tech sector to guide the society’s technical programmes, governance, and research initiatives.', 'Mentoring,Robotics Guidance,Industry Experience', 'finnymentor.jpeg'),
                ('Melvin Joseph', 'Management Tech Team Head', 'Drives management technology strategy while aligning Yantra operations with scalable, intelligent systems.', 'Management,Technology,Strategy', 'management.png'),
                ('Ajmal M S', 'Technical', 'Specializes in technical engineering and robotics prototyping.', 'Engineering,Robotics,Prototyping', 'ajmaltech.jpeg'),
                ('Anirban Mandal', 'Technical', 'Focuses on technical development and system integration.', 'Development,Integration,Robotics', 'anirbantech.jpeg'),
                ('Aryan', 'Technical', 'Contributes to technical innovation and project execution.', 'Innovation,Project Management,Robotics', 'aryantech.jpeg'),
                ('Jishnu Teja Dandamudi', 'Research', 'Leads research initiatives for advanced robotics solutions.', 'Research,Innovation,Analysis', 'jishnuresearch.jpeg'),
                ('Abhay Tiwari', 'Technical', 'Handles technical operations and supports robotics development.', 'Technical Support,Robotics,Operations', 'abhaytech.jpg'),
                ('Jyoti Sharma', 'Technical', 'Contributes to technical development and support.', 'Technical', 'jyotitech.png'),
                ('Vivek Rawat', 'Yantra Admin Council · Coordinator, Tech Lead', 'Electronics Systems member focused on coordination, technical leadership, and brainstorming for Yantra Robotics Society initiatives.', 'Electronics,Leadership,Technical Strategy', 'vivek.jpeg'),
                ('Kural Amuthan M S J', 'Yantra Technical Core', 'Data Science member helping coordinate workshops for schools and supporting outreach activities for Yantra.', 'Workshops,Outreach,Data Science', 'kural.jpg'),
                ('Shubham Chakraborty', 'Yantra Technical Core', 'Data Science member interested in applying deep learning concepts to drone systems and building indigenous autonomous solutions.', 'Deep Learning,Drones,AI Systems', 'shubham.jpg'),
            ]
            for order, (name, role, description, skills, image) in enumerate(roster):
                db.session.add(TeamMember(name=name, role=role, description=description, skills=skills, image_url=f'/img/team/{image}', sort_order=order))
            db.session.commit()

        # Move the homepage's existing event cards into the event catalog.
        if Event.query.count() == 0:
            db.session.add_all([
                Event(title='Embedded Systems Workshop', date=datetime(2026, 3, 18), category='Workshop', location='IIT Madras', description='GPIO, UART & FreeRTOS hands-on | Prof. Viveka K R'),
                Event(title='Robotics Hackathon 2026', date=datetime(2026, 4, 5), category='Hackathon', location='IIT Madras', description='24-hour build | Rs 10k prize | Teams of 2-4'),
                Event(title='AI in Modern Robotics', date=datetime(2026, 4, 22), category='Guest Lecture', location='IIT Madras', description='Foundation models meet real robots | Free entry'),
            ])
            db.session.commit()

        admin_email = os.environ.get('ADMIN_EMAIL')
        admin_password = os.environ.get('ADMIN_PASSWORD')
        admin_name = os.environ.get('ADMIN_NAME')

        admin_role = Role.query.filter_by(name='admin').first()
        editor_role = Role.query.filter_by(name='editor').first()
        member_role = Role.query.filter_by(name='member').first()

        if not admin_role:
            admin_role = Role(name='admin', description='Administrator')
            db.session.add(admin_role)
        if not editor_role:
            editor_role = Role(name='editor', description='Content editor')
            db.session.add(editor_role)
        if not member_role:
            member_role = Role(name='member', description='General member')
            db.session.add(member_role)

        db.session.commit()

        if admin_email and admin_password:
            existing_admin = User.query.filter_by(email=admin_email).first()
            if not existing_admin:
                admin_user = User(
                    name=admin_name,
                    email=admin_email,
                    password=hash_password(admin_password),
                    active=True
                )
                admin_user.roles.append(admin_role)
                db.session.add(admin_user)
                db.session.commit()
                print(f'Created default admin account: {admin_email}')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
