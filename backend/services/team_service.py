from extensions import db
from models import TeamMember
from services.upload_service import cleanup_upload_if_unused

class TeamService:
    @staticmethod
    def get_all():
        return TeamMember.query.filter_by(active=True).order_by(TeamMember.sort_order, TeamMember.id).all()

    @staticmethod
    def get_by_id(member_id):
        return db.session.get(TeamMember, member_id)

    @staticmethod
    def create(data):
        member = TeamMember()
        TeamService.apply(member, data)
        db.session.add(member)
        db.session.commit()
        return member

    @staticmethod
    def update(member_id, data):
        member = TeamService.get_by_id(member_id)
        if member:
            previous_image = member.image_url
            TeamService.apply(member, data)
            db.session.commit()
            if previous_image != member.image_url:
                cleanup_upload_if_unused(previous_image)
        return member

    @staticmethod
    def apply(member, data):
        for key in ('name', 'role', 'description', 'image_url', 'sort_order', 'active'):
            if key in data:
                value = data[key]
                if key in {'name', 'role'} and isinstance(value, str):
                    value = value.strip()
                setattr(member, key, value)
        if 'skills' in data:
            value = data['skills']
            member.skills = ','.join(value) if isinstance(value, list) else (value or '')

    @staticmethod
    def delete(member_id):
        member = TeamService.get_by_id(member_id)
        if not member:
            return False
        previous_image = member.image_url
        db.session.delete(member)
        db.session.commit()
        cleanup_upload_if_unused(previous_image)
        return True
