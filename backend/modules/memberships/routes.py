from flask import Blueprint, request, jsonify
from .models import Membership
from .services import create_membership, list_memberships

membership_bp = Blueprint('membership', __name__)

@membership_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    membership = create_membership(data)
    return jsonify({"id": membership.id}), 201

@membership_bp.route('/', methods=['GET'])
def list_all():
    memberships = list_memberships()
    return jsonify([
        {
            "id": membership.id,
            "user_id": membership.user_id,
            "gym_id": membership.gym_id,
            "start_date": membership.start_date.isoformat(),
            "end_date": membership.end_date.isoformat() if membership.end_date else None,
        } for membership in memberships
    ])
@membership_bp.route('/<int:id>', methods=['GET'])
def get_membership(id):
    membership = Membership.query.get_or_404(id)
    return jsonify({
        "id": membership.id,
        "user_id": membership.user_id,
        "gym_id": membership.gym_id,
        "start_date": membership.start_date.isoformat(),
        "end_date": membership.end_date.isoformat() if membership.end_date else None,
    })