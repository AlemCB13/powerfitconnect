from flask import Blueprint, request, jsonify
from .models import Discipline, Exercise, Workout
from app import db

sports_bp = Blueprint('sports', __name__)

#CRUD for Disciplines
@sports_bp.route('/disciplines', methods=['POST'])
def create_discipline():
    data = request.get_json()
    discipline = Discipline(name=data['name'], description=data.get('description'))
    db.session.add(discipline)
    db.session.commit()
    return jsonify({"id": discipline.id}), 201

@sports_bp.route('/disciplines', methods=['GET'])
def list_disciplines():
    disciplines = Discipline.query.all()
    return jsonify([{"id": d.id, "name": d.name, "description": d.description} for d in disciplines])

@sports_bp.route('/disciplines/<int:id>', methods=['GET'])
def get_discipline(id):
    d = Discipline.query.get_or_404(id)
    return jsonify({"id": d.id, "name": d.name, "description": d.description})

@sports_bp.route('/disciplines/<int:id>', methods=['PUT'])
def update_discipline(id):
    d = Discipline.query.get_or_404(id)
    data = request.get_json()
    d.name = data.get('name', d.name)
    d.description = data.get('description', d.description)
    db.session.commit()
    return jsonify({"id": d.id})

@sports_bp.route('/disciplines/<int:id>', methods=['DELETE'])
def delete_discipline(id):
    d = Discipline.query.get_or_404(id)
    db.session.delete(d)
    db.session.commit()
    return '', 204

#CRUD for Exercises
@sports_bp.route('/exercises', methods=['POST'])
def create_exercise():
    data = request.get_json()
    exercise = Exercise(name=data['name'], description=data.get('description'), discipline_id=data['discipline_id'])
    db.session.add(exercise)
    db.session.commit()
    return jsonify({"id": exercise.id}), 201

@sports_bp.route('/exercises', methods=['GET'])
def list_exercises():
    exercises = Exercise.query.all()
    return jsonify([{"id": e.id, "name": e.name, "description": e.description, "discipline_id": e.discipline_id} for e in exercises])

@sports_bp.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
    e = Exercise.query.get_or_404(id)
    return jsonify({"id": e.id, "name": e.name, "description": e.description, "discipline_id": e.discipline_id})

@sports_bp.route('/exercises/<int:id>', methods=['PUT'])
def update_exercise(id):
    e = Exercise.query.get_or_404(id)
    data = request.get_json()
    e.name = data.get('name', e.name)
    e.description = data.get('description', e.description)
    e.discipline_id = data.get('discipline_id', e.discipline_id)
    db.session.commit()
    return jsonify({"id": e.id})

@sports_bp.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    e = Exercise.query.get_or_404(id)
    db.session.delete(e)
    db.session.commit()
    return '', 204

#CRUD for Workouts
@sports_bp.route('/workouts', methods=['POST'])
def create_workout():
    data = request.get_json()
    workout = Workout(name=data['name'], description=data.get('description'))
    db.session.add(workout)
    db.session.commit()
    return jsonify({"id": workout.id}), 201

@sports_bp.route('/workouts', methods=['GET'])
def list_workouts():
    workouts = Workout.query.all()
    return jsonify([{"id": w.id, "name": w.name, "description": w.description} for w in workouts])

@sports_bp.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    w = Workout.query.get_or_404(id)
    return jsonify({"id": w.id, "name": w.name, "description": w.description})

@sports_bp.route('/workouts/<int:id>', methods=['PUT'])
def update_workout(id):
    w = Workout.query.get_or_404(id)
    data = request.get_json()
    w.name = data.get('name', w.name)
    w.description = data.get('description', w.description)
    db.session.commit()
    return jsonify({"id": w.id})

@sports_bp.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    w = Workout.query.get_or_404(id)
    db.session.delete(w)
    db.session.commit()
    return '', 204

#TODO Add exercises to a workout