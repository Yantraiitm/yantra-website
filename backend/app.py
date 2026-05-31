from flask import Flask, jsonify, request
from flask_cors import CORS
from extensions import db, security
from flask_security import SQLAlchemyUserDatastore, hash_password
from models import User, Role, BlogPost, Application, Event, Course, GalleryImage, ContactMessage
from resources.blog import blog_bp
from resources.events import events_bp
from resources.auth import auth_bp
from resources.team import team_bp
import os

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-yantra')
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

    with app.app_context():
        db.create_all()

        admin_email = os.environ.get('ADMIN_EMAIL', 'admin@yantra.local')
        admin_password = os.environ.get('ADMIN_PASSWORD', 'Admin@123')
        admin_name = os.environ.get('ADMIN_NAME', 'Site Admin')

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