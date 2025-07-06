from .models import Tournament
from .extensions import db
from datetime import datetime

def create_tournament(data):
    date_str = data.get('date')
    date_obj = None
    if date_str:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    tournament = Tournament(
        name=data['name'],
        description=data.get('description'),
        date=date_obj
    )
    db.session.add(tournament)
    db.session.commit()
    return tournament

def get_all_tournaments():
    return Tournament.query.all()

def get_tournament_by_id(id):
    return Tournament.query.get_or_404(id)

def update_tournament(id, data):
    tournament = Tournament.query.get_or_404(id)
    tournament.name = data.get('name', tournament.name)
    tournament.description = data.get('description', tournament.description)
    date_str = data.get('date')
    if date_str:
        tournament.date = datetime.strptime(date_str, '%Y-%m-%d').date()
    db.session.commit()
    return tournament

def delete_tournament(id):
    t = Tournament.query.get_or_404(id)
    db.session.delete(t)
    db.session.commit()