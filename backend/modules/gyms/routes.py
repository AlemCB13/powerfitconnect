from flask import Blueprint, request, jsonify
from .services import create_gym, get_all_gyms, get_gym_by_id, update_gym, delete_gym

gyms_bp = Blueprint('gyms', __name__)

@gyms_bp.route('/', methods=['POST'])
def add_gym():
    data = request.get_json()
    gym = create_gym(
        name=data.get('name'),
        address=data.get('address'),
        phone=data.get('phone'),
        description=data.get('description')
    )
    return jsonify({"id": gym.id, "name": gym.name}), 201

@gyms_bp.route('/', methods=['GET'])
def list_gyms():
    gyms = get_all_gyms()
    return jsonify([{"id": g.id, "name": g.name, "address": g.address, "phone": g.phone, "description": g.description} for g in gyms]), 200

@gyms_bp.route('/<int:gym_id>', methods=['GET'])
def get_gym(gym_id):
    gym = get_gym_by_id(gym_id)
    if not gym:
        return jsonify({"error": "Gym not found"}), 404
    return jsonify({"id": gym.id, "name": gym.name, "address": gym.address, "phone": gym.phone, "description": gym.description}), 200

@gyms_bp.route('/<int:gym_id>', methods=['PUT'])
def edit_gym(gym_id):
    data = request.get_json()
    gym = update_gym(gym_id, data)
    if not gym:
        return jsonify({"msg": "Gym not found"}), 404
    return jsonify({"msg": "Gym updated"})

@gyms_bp.route('/<int:gym_id>', methods=['DELETE'])
def remove_gym(gym_id):
    if not delete_gym(gym_id):
        return jsonify({"msg": "Gym not found"}), 404
    return jsonify({"msg": "Gym deleted"})