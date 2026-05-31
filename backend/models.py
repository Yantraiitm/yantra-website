import uuid

from extensions import db
from flask_security.core import UserMixin, RoleMixin
from datetime import datetime, timezone

class BaseModel(db.Model):
    __abstract__=True
    id= db.Column(db.Integer, primary_key=True)
    created_at=db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at=db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        return {c.name: getattr(self, c.name).isoformat() 
                if isinstance(getattr(self, c.name), datetime) 
                else getattr(self, c.name) 
                for c in self.__table__.columns}

class User(BaseModel, UserMixin):
    __tablename__='users'
    name=db.Column(db.String, nullable=False)
    email=db.Column(db.String, nullable=False, unique=True)
    password=db.Column(db.String, nullable=False)
    fs_uniquifier=db.Column(db.String, unique=True, nullable=False, default=lambda: uuid.uuid4().hex)
    active=db.Column(db.Boolean(), default=True)
    skills = db.Column(db.String(255))
    github_url = db.Column(db.String(255))
    linkedin_url = db.Column(db.String(255))
    image_url = db.Column(db.String(500))

    roles=db.relationship('Role',secondary='user_role',backref='users')

class Role(BaseModel, RoleMixin):
    __tablename__ = 'roles'
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class UserRole(db.Model):
    __tablename__ = 'user_role'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('users.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('roles.id'))

class BlogPost(BaseModel):
    __tablename__ = 'blog_posts'
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(500))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    published = db.Column(db.Boolean(), default=True)

class Application(BaseModel):
    __tablename__ = 'applications'
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20))
    interest_domain = db.Column(db.String(50))
    bio = db.Column(db.Text)
    status = db.Column(db.String(20), default='pending')

class Event(BaseModel):
    __tablename__ = 'events'
    title = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(200))
    description = db.Column(db.Text)
    category = db.Column(db.String(50)) # Workshop, Competition, Lecture

class Course(BaseModel):
    __tablename__ = 'courses'
    title = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(50)) # Beginner, Intermediate, Advanced
    tech_stack = db.Column(db.String(200))
    description = db.Column(db.Text)

class GalleryImage(BaseModel):
    __tablename__ = 'gallery'
    image_url = db.Column(db.String(500), nullable=False)
    caption = db.Column(db.String(200))

class ContactMessage(BaseModel):
    __tablename__ = 'contact_messages'
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    message = db.Column(db.Text)