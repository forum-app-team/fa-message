from flask import Flask, request, redirect, flash
from models.message_models import db
from routes.message_routes import message_bp
from config.config import app_config
import os


def create_app(config_name=None):
    app = Flask(__name__)
    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'development')
    app.config.from_object(app_config[config_name])

    db.init_app(app)

    app.register_blueprint(message_bp)

    return app


if __name__ == "__main__":
    config_name = os.environ.get('FLASK_CONFIG')
    app = create_app(config_name)

    with app.app_context():
        db.create_all()

    app.run(debug=True)
