from flask import jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from .exceptions import AppError


def init_error_handlers(app):
    @app.errorhandler(AppError)
    def handle_app_error(error):
        return jsonify({"error": str(error)}), error.status_code

    @app.errorhandler(ValidationError)
    def handle_validation(error):
        return jsonify({"error": "Validation error"}), 400

    @app.errorhandler(IntegrityError)
    def handle_integrity(error):
        return jsonify({"error": "Constraint violated"}), 400

    @app.errorhandler(SQLAlchemyError)
    def handle_db(error):
        return jsonify({"error": "Database error"}), 500

    @app.errorhandler(Exception)
    def handle_generic(error):
        return jsonify({"error": "Internal server error"}), 500
