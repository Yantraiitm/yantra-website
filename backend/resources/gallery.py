from flask import Blueprint, jsonify, request
from flask_security import auth_required, roles_accepted
from extensions import db
from models import GalleryImage
from services.upload_service import cleanup_upload_if_unused

gallery_bp = Blueprint('gallery', __name__)

@gallery_bp.get('')
def index():
    images = GalleryImage.query.order_by(GalleryImage.sort_order, GalleryImage.id.desc()).all()
    return jsonify([image.to_dict() for image in images])

@gallery_bp.post('')
@auth_required()
@roles_accepted('admin', 'editor')
def create():
    data = request.get_json(silent=True) or {}
    if not data.get('image_url'):
        return jsonify({'error': 'image_url is required'}), 400
    image = GalleryImage(image_url=data['image_url'], caption=data.get('caption'), category=data.get('category', 'general'), sort_order=data.get('sort_order', 0))
    db.session.add(image)
    db.session.commit()
    return jsonify(image.to_dict()), 201

@gallery_bp.route('/<int:image_id>', methods=['PUT', 'DELETE'])
@auth_required()
@roles_accepted('admin', 'editor')
def change(image_id):
    image = db.session.get(GalleryImage, image_id)
    if not image:
        return jsonify({'error': 'Image not found'}), 404
    if request.method == 'DELETE':
        image_url = image.image_url
        db.session.delete(image)
        db.session.commit()
        cleanup_upload_if_unused(image_url)
        return jsonify({'message': 'Image deleted'})
    data = request.get_json(silent=True) or {}
    previous_image = image.image_url
    for key in ('image_url', 'caption', 'category', 'sort_order'):
        if key in data:
            setattr(image, key, data[key])
    db.session.commit()
    if previous_image != image.image_url:
        cleanup_upload_if_unused(previous_image)
    return jsonify(image.to_dict())
