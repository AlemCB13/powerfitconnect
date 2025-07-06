from .models import Discipline, Exercise, Workout
from .extensions import db


# Discipline services
def create_discipline(data):
    discipline = Discipline(name=data['name'], description=data.get('description'))
    db.session.add(discipline)
    db.session.commit()
    return discipline

def get_all_disciplines():
    return Discipline.query.all()

def get_discipline_by_id(id):
    return Discipline.query.get_or_404(id)

def update_discipline(id, data):
    discipline = Discipline.query.get_or_404(id)
    discipline.name = data.get('name', discipline.name)
    discipline.description = data.get('description', discipline.description)
    db.session.commit()
    return discipline

def delete_discipline(id):
    discipline = Discipline.query.get_or_404(id)
    db.session.delete(discipline)
    db.session.commit()

# Exercise services
def create_exercise(data):
    exercise = Exercise(name=data['name'], description=data.get('description'), discipline_id=data['discipline_id'])
    db.session.add(exercise)
    db.session.commit()
    return exercise

def get_all_exercises():
    return Exercise.query.all()

def get_exercise_by_id(id):
    return Exercise.query.get_or_404(id)

def update_exercise(id, data):
    e = Exercise.query.get_or_404(id)
    e.name = data.get('name', e.name)
    e.description = data.get('description', e.description)
    e.discipline_id = data.get('discipline_id', e.discipline_id)
    db.session.commit()
    return e

def delete_exercise(id):
    e = Exercise.query.get_or_404(id)
    db.session.delete(e)
    db.session.commit()

# Workout services
def create_workout(data):
    workout = Workout(name=data['name'], description=data.get('description'))
    db.session.add(workout)
    db.session.commit()
    return workout

def get_all_workouts():
    return Workout.query.all()

def get_workout_by_id(id):
    return Workout.query.get_or_404(id)

def update_workout(id, data):
    w = Workout.query.get_or_404(id)
    w.name = data.get('name', w.name)
    w.description = data.get('description', w.description)
    db.session.commit()
    return w

def delete_workout(id):
    w = Workout.query.get_or_404(id)
    db.session.delete(w)
    db.session.commit()