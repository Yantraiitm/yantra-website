from flask import Blueprint, jsonify, request
from flask_security import auth_required, roles_accepted
from services.team_service import TeamService
from urllib.parse import urlparse

team_bp = Blueprint('team', __name__)

def validate_member(data, partial=False):
    if not isinstance(data, dict): return {'body': 'A JSON object is required.'}
    errors = {}
    for key, label, maximum in (('name', 'Name', 150), ('role', 'Role', 200)):
        if not partial or key in data:
            value = data.get(key)
            if not isinstance(value, str) or not value.strip(): errors[key] = f'{label} is required.'
            elif len(value.strip()) > maximum: errors[key] = f'{label} must be {maximum} characters or fewer.'
    if 'description' in data and data['description'] is not None and not isinstance(data['description'], str): errors['description'] = 'Description must be text.'
    if isinstance(data.get('description'), str) and len(data['description']) > 10000: errors['description'] = 'Description must be 10,000 characters or fewer.'
    if 'image_url' in data and data['image_url'] is not None and (not isinstance(data['image_url'], str) or len(data['image_url']) > 500): errors['image_url'] = 'Image URL must be at most 500 characters.'
    if isinstance(data.get('image_url'), str) and data['image_url']:
        try:
            parsed = urlparse(data['image_url'])
            valid_external = parsed.scheme in {'http', 'https'} and bool(parsed.netloc)
        except ValueError:
            valid_external = False
        if not valid_external and not data['image_url'].startswith(('/img/', '/api/uploads/')):
            errors['image_url'] = 'Use an HTTP/HTTPS URL or a local image path.'
    if 'skills' in data:
        skills = data['skills']
        if not isinstance(skills, (str, list)) or (isinstance(skills, list) and (len(skills) > 30 or any(not isinstance(skill, str) or len(skill) > 60 for skill in skills))): errors['skills'] = 'Skills must be text or a list of up to 30 short strings.'
    if 'sort_order' in data and (isinstance(data['sort_order'], bool) or not isinstance(data['sort_order'], int)): errors['sort_order'] = 'Sort order must be a whole number.'
    if 'sort_order' in data and isinstance(data['sort_order'], int) and not isinstance(data['sort_order'], bool) and abs(data['sort_order']) > 1000000: errors['sort_order'] = 'Sort order is outside the supported range.'
    if 'active' in data and not isinstance(data['active'], bool): errors['active'] = 'Active must be true or false.'
    return errors

@team_bp.route('', methods=['GET'])
def index():
    return jsonify([m.to_dict() for m in TeamService.get_all()])

@team_bp.route('/<int:member_id>', methods=['GET'])
def show(member_id):
    member = TeamService.get_by_id(member_id)
    return jsonify(member.to_dict()) if member else (jsonify({"error": "Member not found"}), 404)

@team_bp.route('/<int:member_id>', methods=['PUT'])
@auth_required()
@roles_accepted('admin')
def update(member_id):
    data = request.get_json(silent=True)
    errors = validate_member(data, partial=True)
    if not errors and not data: errors['body'] = 'Provide at least one field to update.'
    if errors: return jsonify({'error': 'Team member details are invalid.', 'details': errors}), 400
    member = TeamService.update(member_id, data)
    return jsonify(member.to_dict()) if member else (jsonify({"error": "Member not found"}), 404)

@team_bp.route('', methods=['POST'])
@auth_required()
@roles_accepted('admin')
def create():
    data = request.get_json(silent=True)
    errors = validate_member(data)
    if errors: return jsonify({'error': 'Team member details are invalid.', 'details': errors}), 400
    member = TeamService.create(data)
    return jsonify(member.to_dict()), 201

@team_bp.route('/<int:member_id>', methods=['DELETE'])
@auth_required()
@roles_accepted('admin')
def delete(member_id):
    success = TeamService.delete(member_id)
    if not success:
        return jsonify({"error": "Member not found"}), 404
    return jsonify({"message": "Member deleted"})
