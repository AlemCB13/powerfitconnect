from .models import Membership
from .extensions import db
import datetime

def create_membership(data):
    data ['start_date'] = datetime.datetime.strptime(data['start_date'], "%Y-%m-%d").date()  # Ensure date is in correct format
    data ['end_date'] = datetime.datetime.strptime(data['end_date'], "%Y-%m-%d").date()
    membership = Membership(**data)
    db.session.add(membership)
    db.session.commit()
    return membership

def list_memberships():
    return Membership.query.all()