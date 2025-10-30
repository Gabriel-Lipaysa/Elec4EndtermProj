from app.models.user import User
from app import bcrypt

def authenticate_user(username,password):
    user = User.query.filter_by(username=username, role='admin').first()
    if user and bcrypt.check_password_hash(user.password,password):
        return user
    return None