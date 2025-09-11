from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Message(db.Model):
    __tablename__ = "messages"

    messageId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)
    dateCreated = db.Column(
        db.DateTime, default=datetime.now, nullable=False)
    status = db.Column(db.String(20), default='open', nullable=False)

    def to_dict(self):
        return {
            'messageId': self.messageId,
            'userId': self.userId,
            'email': self.email,
            'message': self.message,
            'dateCreated': self.dateCreated.isoformat(),
            'status': self.status
        }

    def __repr__(self):
        return f"Message (messageId={self.messageId!r})"
