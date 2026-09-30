from pathlib import Path
from uuid import uuid4

from flask import Blueprint, current_app, jsonify, request, url_for
from flask_security import auth_required, roles_accepted
from werkzeug.utils import secure_filename

uploads_bp = Blueprint('uploads', __name__)
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

@uploads_bp.post('')
@auth_required()
@roles_accepted('admin', 'editor')
def upload():
    uploaded = request.files.get('file')
    if not uploaded or not uploaded.filename:
        return jsonify({'error': 'Choose a JPG or PNG image.'}), 400

    original_name = secure_filename(uploaded.filename)
    extension = Path(original_name).suffix.lower().lstrip('.')
    if extension not in ALLOWED_EXTENSIONS:
        return jsonify({'error': 'Only JPG and PNG images are supported.'}), 400
    if uploaded.mimetype not in {'image/jpeg', 'image/png'}:
        return jsonify({'error': 'The uploaded file must be a JPG or PNG image.'}), 400
    signature = uploaded.stream.read(8)
    uploaded.stream.seek(0)
    valid_jpeg = signature.startswith(b'\xff\xd8\xff')
    valid_png = signature.startswith(b'\x89PNG\r\n\x1a\n')
    if not (valid_jpeg if extension in {'jpg', 'jpeg'} else valid_png):
        return jsonify({'error': 'The file contents do not match its image type.'}), 400

    upload_dir = Path(current_app.root_path) / 'uploads'
    upload_dir.mkdir(parents=True, exist_ok=True)
    filename = f'{uuid4().hex}.{extension}'
    uploaded.save(upload_dir / filename)
    return jsonify({'image_url': url_for('uploaded_file', filename=filename, _external=True)}), 201
