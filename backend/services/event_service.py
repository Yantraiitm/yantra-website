from datetime import datetime, timezone
from sqlalchemy import func, text

from extensions import db
from models import Event, EventRegistration
from services.upload_service import cleanup_upload_if_unused

EVENT_FIELDS = {'title', 'date', 'location', 'description', 'category', 'image_url', 'registration_url', 'max_attendees'}

class RegistrationConflict(Exception):
    pass

def parse_date(value):
    if isinstance(value, datetime):
        parsed = value
    elif isinstance(value, str):
        try:
            parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
        except ValueError as error:
            raise ValueError('date must be a valid ISO 8601 date and time') from error
    else:
        raise ValueError('date is required and must be an ISO 8601 date and time')
    if parsed.tzinfo:
        parsed = parsed.astimezone(timezone.utc).replace(tzinfo=None)
    return parsed

class EventService:
    @staticmethod
    def get_all():
        return Event.query.order_by(Event.date.asc()).all()

    @staticmethod
    def get_by_id(event_id):
        return db.session.get(Event, event_id)

    @staticmethod
    def as_dict(event):
        result = event.to_dict()
        registered = EventRegistration.query.filter_by(event_id=event.id).count()
        date = event.date.replace(tzinfo=timezone.utc) if event.date.tzinfo is None else event.date
        now = datetime.now(timezone.utc)
        result['registered_attendees'] = registered
        result['registration_status'] = 'past' if date < now else ('full' if event.max_attendees is not None and registered >= event.max_attendees else 'open')
        result['seats_remaining'] = None if event.max_attendees is None else max(event.max_attendees - registered, 0)
        return result

    @staticmethod
    def create(data):
        event_date = parse_date(data.get('date'))

        event = Event(
            title=data.get('title').strip(),
            date=event_date,
            location=data.get('location'),
            description=data.get('description'),
            category=data.get('category'),
            image_url=data.get('image_url'),
            registration_url=data.get('registration_url'),
            max_attendees=data.get('max_attendees')
        )
        db.session.add(event)
        db.session.commit()
        return event

    @staticmethod
    def update(event_id, data):
        event = Event.query.get(event_id)
        if event:
            previous_image = event.image_url
            for key, value in data.items():
                if key in EVENT_FIELDS:
                    if key == 'date':
                        value = parse_date(value)
                    elif key == 'title' and isinstance(value, str):
                        value = value.strip()
                    setattr(event, key, value)
            db.session.commit()
            if previous_image != event.image_url:
                cleanup_upload_if_unused(previous_image)
        return event

    @staticmethod
    def delete(event_id):
        event = Event.query.get(event_id)
        if event:
            previous_image = event.image_url
            db.session.delete(event)
            db.session.commit()
            cleanup_upload_if_unused(previous_image)
            return True
        return False

    @staticmethod
    def register(event, data):
        # SQLite's immediate write lock keeps simultaneous requests from exceeding capacity.
        event_id = event.id
        email = data['email'].strip().lower()
        db.session.rollback()
        db.session.execute(text('BEGIN IMMEDIATE'))
        event = db.session.get(Event, event_id)
        if not event:
            db.session.rollback()
            raise RegistrationConflict('Event not found.')
        registered = db.session.query(func.count(EventRegistration.id)).filter_by(event_id=event_id).scalar()
        event_date = event.date.replace(tzinfo=timezone.utc) if event.date.tzinfo is None else event.date
        if event_date < datetime.now(timezone.utc):
            db.session.rollback()
            raise RegistrationConflict('Registration is closed because this event has passed.')
        if event.max_attendees is not None and registered >= event.max_attendees:
            db.session.rollback()
            raise RegistrationConflict('This event is full.')
        if EventRegistration.query.filter_by(event_id=event_id, email=email).first():
            db.session.rollback()
            raise RegistrationConflict('This email is already registered for the event.')
        registration = EventRegistration(event_id=event_id, name=data['name'].strip(), email=email, phone=(data.get('phone') or '').strip() or None)
        db.session.add(registration)
        db.session.commit()
        return registration
