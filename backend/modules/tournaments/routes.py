from flask import Blueprint, request, jsonify
from .services import (
    create_tournament,
    get_all_tournaments,
    get_tournament_by_id,
    update_tournament,
    delete_tournament
)

tournaments_bp = Blueprint('tournaments', __name__)

@tournaments_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    t = create_tournament(data)
    return jsonify({"id": t.id}), 201

@tournaments_bp.route('/', methods=['GET'])
def list_all():
    tournaments = get_all_tournaments()
    return jsonify([
        {"id": t.id, "name": t.name, "description": t.description, "date": str(t.date)}
        for t in tournaments
    ])

@tournaments_bp.route('/<int:id>', methods=['GET'])
def get(id):
    t = get_tournament_by_id(id)
    return jsonify({"id": t.id, "name": t.name, "description": t.description, "date": str(t.date)})

@tournaments_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    t = update_tournament(id, data)
    return jsonify({"id": t.id})

@tournaments_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    delete_tournament(id)
    return '', 204