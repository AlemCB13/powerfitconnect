from flask import Flask
from flask_cors import CORS
from .extensions import db, migrate
from .routes import tournaments_bp

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tournaments.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    app.register_blueprint(tournaments_bp, url_prefix='/tournaments')
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)