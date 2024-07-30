from flask import Flask
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions (e.g., SQLAlchemy, Migrate)
    # db.init_app(app)
    # migrate.init_app(app, db)

    # Register blueprints
    # from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    return app

