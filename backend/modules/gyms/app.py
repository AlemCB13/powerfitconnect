python
from flask import Flask
from flask_cors import CORS
from .routes import gyms_bp
from .extensions import db, migrate

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///gyms.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    app.register_blueprint(gyms_bp, url_prefix='/gyms')
    return app

app = create_app()