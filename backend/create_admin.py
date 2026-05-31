import argparse
import uuid
from app import create_app
from extensions import db
from flask_security import hash_password
from models import User, Role


def create_admin(email, password, name):
    app = create_app()
    with app.app_context():
        db.create_all()

        admin_role = Role.query.filter_by(name='admin').first()
        if not admin_role:
            admin_role = Role(name='admin', description='Administrator')
            db.session.add(admin_role)
            db.session.commit()

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            print(f"User with email '{email}' already exists.")
            return

        user = User(
            name=name,
            email=email,
            password=hash_password(password),
            fs_uniquifier=uuid.uuid4().hex,
            active=True
        )
        user.roles.append(admin_role)
        db.session.add(user)
        db.session.commit()

        print('Admin user created successfully:')
        print(f'  email: {email}')
        print(f'  name: {name}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create an admin user in the Yantra backend database.')
    parser.add_argument('--email', required=True, help='Admin email address')
    parser.add_argument('--password', required=True, help='Admin password')
    parser.add_argument('--name', default='Site Admin', help='Admin display name')
    args = parser.parse_args()

    create_admin(args.email, args.password, args.name)
