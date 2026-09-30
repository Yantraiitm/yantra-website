from pathlib import Path
from urllib.parse import urlparse

from flask import current_app

from models import Event, GalleryImage, TeamMember


def uploaded_filename(image_url):
    """Return a safe managed-upload filename, or None for static/external images."""
    if not isinstance(image_url, str) or not image_url:
        return None
    try:
        path = urlparse(image_url).path
    except ValueError:
        return None
    if not path.startswith('/api/uploads/'):
        return None
    filename = Path(path).name
    stem, extension = Path(filename).stem, Path(filename).suffix.lower()
    if len(stem) != 32 or any(char not in '0123456789abcdef' for char in stem) or extension not in {'.jpg', '.jpeg', '.png'}:
        return None
    return filename


def cleanup_upload_if_unused(image_url):
    """Remove a stored upload after the last database record stops referring to it."""
    filename = uploaded_filename(image_url)
    if not filename:
        return False

    suffix = f'/{filename}'
    references = (
        TeamMember.query.filter(TeamMember.image_url.endswith(suffix)).first(),
        Event.query.filter(Event.image_url.endswith(suffix)).first(),
        GalleryImage.query.filter(GalleryImage.image_url.endswith(suffix)).first(),
    )
    if any(references):
        return False

    upload_path = Path(current_app.root_path, 'uploads', filename)
    try:
        upload_path.unlink(missing_ok=True)
    except OSError:
        current_app.logger.exception('Could not remove uploaded image %s', filename)
        return False
    return True
