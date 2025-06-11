from .models import User
from app import db

def register_user(username, password):
    if User.query.filter_by(username=username).first():
        return None, "Username already exists"
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return User, None

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user, None
    return None, "Invalid username or password"