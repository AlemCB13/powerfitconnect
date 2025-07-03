from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config

db = SQLAlchemy()
migrate = Migrate(db)
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)

    #import blueprints
    from modules.auth.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    #import gyms blueprint
    from modules.gyms.routes import gyms_bp
    app.register_blueprint(gyms_bp, url_prefix='/gyms')
    #import memberships blueprint
    from modules.memberships.routes import membership_bp
    app.register_blueprint(membership_bp, url_prefix='/memberships')
    #import sports blueprint
    from modules.sports.routes import sports_bp
    app.register_blueprint(sports_bp, url_prefix='/sports')

    @app.route('/api/health')
    def health():
        return {"status": "ok"}, 200
    return app

#Flask run 
app = create_app()