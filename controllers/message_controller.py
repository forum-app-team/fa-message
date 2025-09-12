from flask import request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from marshmallow import ValidationError
from services.message_service import MessageService
from exceptions.exceptions import NotFoundException, DuplicateException
from schemas.message_schema import MessageSchema


schema = MessageSchema()
limiter = Limiter(key_func=get_remote_address)
service = MessageService()


def get_all_messages():
    try:
        messages = service.get_all()
        return jsonify({"data": [m.to_dict() for m in messages]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def get_message_by_id(message_id):
    try:
        message = service.get_by_id(message_id)
        return jsonify({"data": message.to_dict()}), 200
    except NotFoundException:
        return jsonify({"error": "Message not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@limiter.limit("5/minute")
def send_message():
    data = request.get_json()
    try:
        validated_data = schema.load(data or {})
        message = service.create(validated_data)
        return jsonify({"data": message.to_dict()}), 201
    except ValidationError as e:
        return jsonify({"error": "Validation error"}), 400
    except DuplicateException:
        return jsonify({"error": "Duplicate message detected"}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500
