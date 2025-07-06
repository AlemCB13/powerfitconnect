from .extensions import db

class Membership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # gym_id = db.Column(db.Integer, db.ForeignKey('gym.id'), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    gym_id = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

    # user = db.relationship('User', backref='memberships')
    # gym = db.relationship('Gym', backref='memberships')

    def __repr__(self):
        return f'<Membership {self.id} for User {self.user_id} at Gym {self.gym_id}>'