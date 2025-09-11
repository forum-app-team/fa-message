from flask import request, jsonify
from models.message_models import db, Message


def get_all_messages():
    try:
        messages = Message.query.order_by(Message.dateCreated.desc()).all()

        return jsonify({"data": [message.to_dict() for message in messages]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def get_message_by_id(message_id):
    try:
        message = db.session.get(Message, message_id)
        if not message:
            return jsonify({'error': 'Message not found'}), 404

        return jsonify({'data': message.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def send_message():
    try:
        data = request.get_json()

        for field in ("userId", "email", "message"):
            if field not in data:
                return jsonify({"error": f"{field} is required"}), 400

        new_message = Message(
            userId=int(data['userId']),  # type: ignore
            email=data['email'],  # type: ignore
            message=data['message'],  # type: ignore
            status=data.get('status', 'open')  # type: ignore
        )

        db.session.add(new_message)
        db.session.commit()

        return jsonify({
            'message': 'Message sent successfully',
            'data': new_message.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
