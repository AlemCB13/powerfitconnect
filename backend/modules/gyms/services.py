from .models import Gym
from app import db

def create_gym(name, address, phone=None, description=None):
    gym = Gym(name=name, address=address, phone=phone, description=description)
    db.session.add(gym)
    db.session.commit()
    return gym

def get_all_gyms():
    return Gym.query.all()

def get_gym_by_id(gym_id):
    return Gym.query.get(gym_id)

def update_gym(gym_id, gym_data):
    gym = Gym.query.get(gym_id)
    if not gym:
        return None
    for key, value in gym_data.items():
        setattr(gym, key, value)
    db.session.commit()
    return gym

def delete_gym(gym_id):
    gym = Gym.query.get(gym_id)
    if not gym:
        return None
    db.session.delete(gym)
    db.session.commit()
    return True