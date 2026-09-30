from flask import Blueprint, jsonify, request
from flask_security import auth_required, roles_accepted
from sqlalchemy.exc import IntegrityError
import re
from datetime import datetime, timezone
from urllib.parse import urlparse
from services.event_service import EventService, RegistrationConflict, parse_date

events_bp = Blueprint('events', __name__)

@events_bp.route('', methods=['GET'])
def index():
    events = EventService.get_all()
    return jsonify([EventService.as_dict(event) for event in events])

@events_bp.route('/<int:event_id>', methods=['GET'])
def show(event_id):
    event = EventService.get_by_id(event_id)
    return jsonify(EventService.as_dict(event)) if event else (jsonify({'error': 'Event not found'}), 404)

def validate_event(data, partial=False):
    if not isinstance(data, dict):
        return {'body': 'A JSON object is required.'}
    errors = {}
    if not partial or 'title' in data:
        if not isinstance(data.get('title'), str) or not data['title'].strip(): errors['title'] = 'Title is required.'
        elif len(data['title'].strip()) > 200: errors['title'] = 'Title must be 200 characters or fewer.'
    if not partial or 'date' in data:
        try: parse_date(data.get('date'))
        except (ValueError, TypeError): errors['date'] = 'Provide a valid ISO 8601 date and time.'
    if 'max_attendees' in data or not partial:
        limit = data.get('max_attendees')
        if limit is not None and (isinstance(limit, bool) or not isinstance(limit, int) or limit < 1): errors['max_attendees'] = 'Attendee limit must be a positive whole number or blank.'
    for key, max_length in (('location', 200), ('category', 50), ('image_url', 500), ('registration_url', 500)):
        value = data.get(key)
        if value is not None and (not isinstance(value, str) or len(value) > max_length): errors[key] = f'{key.replace("_", " ").capitalize()} must be at most {max_length} characters.'
    if data.get('description') is not None and not isinstance(data['description'], str): errors['description'] = 'Description must be text.'
    if isinstance(data.get('description'), str) and len(data['description']) > 10000: errors['description'] = 'Description must be 10,000 characters or fewer.'
    for key in ('image_url', 'registration_url'):
        value = data.get(key)
        if isinstance(value, str) and value:
            try:
                parsed = urlparse(value)
                valid_external = parsed.scheme in {'http', 'https'} and bool(parsed.netloc)
            except ValueError:
                valid_external = False
            if not valid_external and not value.startswith(('/img/', '/api/uploads/')):
                errors[key] = 'Use an HTTP/HTTPS URL or a local image path.'
    return errors

@events_bp.post('/<int:event_id>/registrations')
def register(event_id):
    event = EventService.get_by_id(event_id)
    if not event:
        return jsonify({'error': 'Event not found.'}), 404
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({'error': 'A JSON object is required.'}), 400
    errors = {}
    name, email, phone = data.get('name'), data.get('email'), data.get('phone', '')
    if not isinstance(name, str) or not name.strip() or len(name.strip()) > 150: errors['name'] = 'Enter a name up to 150 characters.'
    if not isinstance(email, str) or len(email) > 254 or not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+', email.strip()): errors['email'] = 'Enter a valid email address.'
    if not isinstance(phone, str) or len(phone) > 32: errors['phone'] = 'Phone must be 32 characters or fewer.'
    if errors: return jsonify({'error': 'Please correct the registration details.', 'details': errors}), 400
    if event.date.replace(tzinfo=None) < datetime.now(timezone.utc).replace(tzinfo=None):
        return jsonify({'error': 'Registration is closed because this event has passed.'}), 409
    if event.max_attendees is not None and len(event.registrations) >= event.max_attendees:
        return jsonify({'error': 'This event is full.'}), 409
    if any(item.email.lower() == email.strip().lower() for item in event.registrations):
        return jsonify({'error': 'This email is already registered for the event.'}), 409
    try:
        attendee = EventService.register(event, data)
    except RegistrationConflict as error:
        return jsonify({'error': str(error)}), 409
    except IntegrityError:
        from extensions import db
        db.session.rollback()
        return jsonify({'error': 'This email is already registered for the event.'}), 409
    return jsonify({'message': 'Registration confirmed.', 'registration_id': attendee.id, 'event': EventService.as_dict(event)}), 201

@events_bp.get('/<int:event_id>/attendees')
@auth_required()
@roles_accepted('admin', 'editor')
def attendees(event_id):
    event = EventService.get_by_id(event_id)
    if not event: return jsonify({'error': 'Event not found.'}), 404
    return jsonify([{'id': row.id, 'name': row.name, 'email': row.email, 'phone': row.phone, 'registered_at': row.created_at.isoformat() if row.created_at else None} for row in event.registrations])

@events_bp.route('', methods=['POST'])
@auth_required()
@roles_accepted('admin', 'editor')
def create():
    data = request.get_json(silent=True)
    errors = validate_event(data)
    if errors: return jsonify({'error': 'Event details are invalid.', 'details': errors}), 400
    try: event = EventService.create(data)
    except ValueError as error: return jsonify({'error': str(error), 'details': {'date': str(error)}}), 400
    return jsonify(EventService.as_dict(event)), 201

@events_bp.route('/<int:event_id>', methods=['PUT'])
@auth_required()
@roles_accepted('admin', 'editor')
def update(event_id):
    data = request.get_json(silent=True)
    errors = validate_event(data, partial=True)
    if not errors and not data: errors['body'] = 'Provide at least one field to update.'
    if errors: return jsonify({'error': 'Event details are invalid.', 'details': errors}), 400
    try: event = EventService.update(event_id, data)
    except ValueError as error: return jsonify({'error': str(error), 'details': {'date': str(error)}}), 400
    return jsonify(EventService.as_dict(event)) if event else (jsonify({'error': 'Event not found.'}), 404)

@events_bp.route('/<int:event_id>', methods=['DELETE'])
@auth_required()
@roles_accepted('admin')
def delete(event_id):
    success = EventService.delete(event_id)
    if not success:
        return jsonify({'error': 'Event not found'}), 404
    return jsonify({'message': 'Event deleted'})
