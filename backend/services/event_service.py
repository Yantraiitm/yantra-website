from datetime import datetime

from extensions import db
from models import Event

class EventService:
    @staticmethod
    def get_all():
        return Event.query.order_by(Event.date.asc()).all()

    @staticmethod
    def get_by_id(event_id):
        return Event.query.get(event_id)

    @staticmethod
    def create(data):
        event_date = data.get('date')
        if isinstance(event_date, str):
            event_date = datetime.fromisoformat(event_date)

        event = Event(
            title=data.get('title'),
            date=event_date,
            location=data.get('location'),
            description=data.get('description'),
            category=data.get('category')
        )
        db.session.add(event)
        db.session.commit()
        return event

    @staticmethod
    def update(event_id, data):
        event = Event.query.get(event_id)
        if event:
            if 'date' in data and isinstance(data['date'], str):
                data['date'] = datetime.fromisoformat(data['date'])
            for key, value in data.items():
                if hasattr(event, key):
                    setattr(event, key, value)
            db.session.commit()
        return event

    @staticmethod
    def delete(event_id):
        event = Event.query.get(event_id)
        if event:
            db.session.delete(event)
            db.session.commit()
            return True
        return False
