from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
from sqlalchemy.sql import func

db = SQLAlchemy()


class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    subject = db.Column(db.String(255), nullable=False)
    message = db.Column(db.String(1000), nullable=False)
    date_created = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    status = db.Column(db.String(20), default="pending", nullable=False)

    __table_args__ = (
        CheckConstraint(
            "status IN ('pending','opened','closed')", name="ck_messages_status_allowed"
        ),
    )

    def to_dict(self):
        datetime_created = self.date_created.isoformat() if self.date_created else None
        return {
            "id": self.id,
            "email": self.email,
            "subject": self.subject,
            "message": self.message,
            "date_created": datetime_created,
            "status": self.status,
        }

    def __repr__(self):
        return f"<Message (id={self.id!r} status={self.status!r})>"
