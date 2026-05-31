from flask import Blueprint, jsonify, request
from flask_security import auth_required, roles_accepted
from services.blog_service import BlogService

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('', methods=['GET'])
def index():
    posts = BlogService.get_all()
    return jsonify([p.to_dict() for p in posts])

@blog_bp.route('/<int:post_id>', methods=['GET'])
def show(post_id):
    post = BlogService.get_by_id(post_id)
    return jsonify(post.to_dict()) if post else (jsonify({"error": "Not found"}), 404)

@blog_bp.route('', methods=['POST'])
@auth_required()
@roles_accepted('admin', 'editor')
def create():
    data = request.json
    post = BlogService.create(data)
    return jsonify(post.to_dict()), 201

@blog_bp.route('/<int:post_id>', methods=['PUT'])
@auth_required()
@roles_accepted('admin', 'editor')
def update(post_id):
    data = request.json
    post = BlogService.update(post_id, data)
    return jsonify(post.to_dict()) if post else (jsonify({"error": "Not found"}), 404)

@blog_bp.route('/<int:post_id>', methods=['DELETE'])
@auth_required()
@roles_accepted('admin')
def delete(post_id):
    success = BlogService.delete(post_id)
    return jsonify({"message": "Deleted"}), 200 if success else (jsonify({"error": "Not found"}), 404)