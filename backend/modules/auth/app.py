from flask import Flask
from .extensions import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .routes import auth_bp

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///auth.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'your-very-secret-key'  # Change this in production

db = db
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    return app

app = create_app()