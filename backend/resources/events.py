from flask import Blueprint, jsonify, request
from flask_security import auth_required, roles_accepted
from services.event_service import EventService

events_bp = Blueprint('events', __name__)

@events_bp.route('', methods=['GET'])
def index():
    events = EventService.get_all()
    return jsonify([event.to_dict() for event in events])

@events_bp.route('/<int:event_id>', methods=['GET'])
def show(event_id):
    event = EventService.get_by_id(event_id)
    return jsonify(event.to_dict()) if event else (jsonify({'error': 'Event not found'}), 404)

@events_bp.route('', methods=['POST'])
@auth_required()
@roles_accepted('admin', 'editor')
def create():
    data = request.json
    event = EventService.create(data)
    return jsonify(event.to_dict()), 201

@events_bp.route('/<int:event_id>', methods=['PUT'])
@auth_required()
@roles_accepted('admin', 'editor')
def update(event_id):
    data = request.json
    event = EventService.update(event_id, data)
    return jsonify(event.to_dict()) if event else (jsonify({'error': 'Event not found'}), 404)

@events_bp.route('/<int:event_id>', methods=['DELETE'])
@auth_required()
@roles_accepted('admin')
def delete(event_id):
    success = EventService.delete(event_id)
    return jsonify({'message': 'Event deleted'}) if success else (jsonify({'error': 'Event not found'}), 404)
