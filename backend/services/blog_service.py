from extensions import db
from models import BlogPost

class BlogService:
    @staticmethod
    def get_all():
        return BlogPost.query.order_by(BlogPost.created_at.desc()).all()

    @staticmethod
    def get_by_id(post_id):
        return BlogPost.query.get(post_id)

    @staticmethod
    def create(data):
        post = BlogPost(
            title=data.get('title'),
            content=data.get('content'),
            image_url=data.get('image_url'),
            author_id=data.get('author_id'),
            published=data.get('published', True)
        )
        db.session.add(post)
        db.session.commit()
        return post

    @staticmethod
    def update(post_id, data):
        post = BlogPost.query.get(post_id)
        if post:
            post.title = data.get('title', post.title)
            post.content = data.get('content', post.content)
            post.image_url = data.get('image_url', post.image_url)
            post.published = data.get('published', post.published)
            db.session.commit()
        return post

    @staticmethod
    def delete(post_id):
        post = BlogPost.query.get(post_id)
        if post:
            db.session.delete(post)
            db.session.commit()
            return True
        return False