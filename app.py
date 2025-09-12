import os
from flask import Flask
from config.config import app_config
from models.message_model import db
from routes.message_routes import message_bp
from exceptions.error_handlers import init_error_handlers


def create_app(config_name=None):
    app = Flask(__name__)
    if config_name is None:
        config_name = os.environ.get("FLASK_CONFIG", "development")
    app.config.from_object(app_config[config_name])

    # Extensions
    db.init_app(app)

    # Blueprints
    app.register_blueprint(message_bp)

    # Error handler
    init_error_handlers(app)

    @app.teardown_request
    def teardown_db(exception):
        db.session.remove()

    return app


if __name__ == "__main__":
    config_name = os.environ.get("FLASK_CONFIG")
    app = create_app(config_name)

    with app.app_context():
        db.create_all()

    app.run(port=3003, debug=True)
