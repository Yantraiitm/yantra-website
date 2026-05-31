from flask import Blueprint, jsonify, request
from flask_security import auth_required, roles_accepted
from services.team_service import TeamService

team_bp = Blueprint('team', __name__)

@team_bp.route('', methods=['GET'])
def index():
    members = TeamService.get_all()
    # We map 'roles' into the dict so the frontend knows their designation
    return jsonify([{
        **m.to_dict(),
        "designations": [r.name for r in m.roles]
    } for m in members])

@team_bp.route('/<int:member_id>', methods=['GET'])
def show(member_id):
    member = TeamService.get_by_id(member_id)
    return jsonify(member.to_dict()) if member else (jsonify({"error": "Member not found"}), 404)

@team_bp.route('', methods=['POST'])
@auth_required()
@roles_accepted('admin')
def create():
    data = request.json
    member = TeamService.create(data)
    return jsonify(member.to_dict()), 201

@team_bp.route('/<int:member_id>', methods=['PUT'])
@auth_required()
@roles_accepted('admin')
def update(member_id):
    data = request.json
    member = TeamService.update(member_id, data)
    return jsonify(member.to_dict()) if member else (jsonify({"error": "Member not found"}), 404)

@team_bp.route('/<int:member_id>', methods=['DELETE'])
@auth_required()
@roles_accepted('admin')
def delete(member_id):
    success = TeamService.delete(member_id)
    return jsonify({"message": "Member deleted"}), 200 if success else (jsonify({"error": "Member not found"}), 404)