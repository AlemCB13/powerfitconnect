from .extensions import db

class Gym(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(30))
    description = db.Column(db.Text)
    # image_url = db.Column(db.String(200), nullable=True) # Uncomment if you want to store image URLs