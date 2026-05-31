from flask import Blueprint, jsonify, request
from flask_security import auth_required, current_user, login_user
from flask_security.utils import verify_password
from models import User

auth_bp = Blueprint('auth_api', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Handles user login. Returns an authentication token and user profile.
    Registration is disabled; users are managed as team members.
    """
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=data.get('email')).first()

    if user and verify_password(data.get('password'), user.password):
        if not user.active:
            return jsonify({"error": "Account is inactive"}), 403

        login_user(user)
        token = user.get_auth_token()

        return jsonify({
            "token": token,
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "roles": [role.name for role in user.roles]
            }
        }), 200

    return jsonify({"error": "Invalid email or password"}), 401

@auth_bp.route('/me', methods=['GET'])
@auth_required('session', 'token')
def me():
    """
    Returns the current authenticated user's profile and roles.
    Used by the Vue frontend to sync state.
    """
    return jsonify({
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "roles": [role.name for role in current_user.roles],
        "skills": current_user.skills,
        "github_url": current_user.github_url,
        "linkedin_url": current_user.linkedin_url,
        "image_url": current_user.image_url
    })