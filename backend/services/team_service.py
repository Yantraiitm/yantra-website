from extensions import db
from flask_security import hash_password
from models import Role, User

class TeamService:
    @staticmethod
    def get_all():
        return User.query.filter_by(active=True).all()

    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def create(data):
        password = data.get('password', 'ChangeMe123!')
        user = User(
            name=data.get('name'),
            email=data.get('email'),
            password=hash_password(password),
            skills=data.get('skills'),
            github_url=data.get('github_url'),
            linkedin_url=data.get('linkedin_url'),
            image_url=data.get('image_url'),
            active=True
        )

        role_names = data.get('roles', ['member'])
        if isinstance(role_names, str):
            role_names = [role_names]

        for role_name in role_names:
            role = Role.query.filter_by(name=role_name).first()
            if role:
                user.roles.append(role)

        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def update(user_id, data):
        user = User.query.get(user_id)
        if user:
            if 'password' in data and data['password']:
                user.password = hash_password(data['password'])

            if 'roles' in data:
                user.roles = []
                role_names = data['roles']
                if isinstance(role_names, str):
                    role_names = [role_names]
                for role_name in role_names:
                    role = Role.query.filter_by(name=role_name).first()
                    if role:
                        user.roles.append(role)

            for key, value in data.items():
                if key in {'name', 'email', 'skills', 'github_url', 'linkedin_url', 'image_url', 'active'}:
                    setattr(user, key, value)
            db.session.commit()
        return user

    @staticmethod
    def delete(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False

    @staticmethod
    def deactivate(user_id):
        user = User.query.get(user_id)
        if user:
            user.active = False
            db.session.commit()
            return True
        return False