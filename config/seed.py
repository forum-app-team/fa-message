import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app import create_app
from models.message_model import db, Message
from datetime import datetime, timedelta
import random


def create_mock_data():
    emails = [
        "john.doe@example.com",
        "jane.smith@example.com",
        "mike.wilson@example.com",
        "sarah.jones@example.com",
        "alex.brown@example.com",
    ]

    subjects = [
        "Feedback",
        "Account credential lost",
        "Account got hacked",
        "Appreciation",
    ]

    sample_messages = [
        "Hello everyone! Welcome to the forum.",
        "Has anyone tried the new feature?",
        "I'm having trouble with my account settings.",
        "Great discussion in yesterday's meeting!",
        "Looking forward to the next update.",
        "Can someone help me with this issue?",
        "Thanks for the quick response!",
        "The documentation is very helpful.",
        "When is the next release scheduled?",
        "Love the new interface design!",
    ]

    statuses = ["opened", "closed", "pending"]

    messages = []
    for i in range(5):
        days_ago = random.randint(0, 30)
        created_date = datetime.now() - timedelta(days=days_ago)

        message = Message(
            subject=random.choice(subjects),  # type: ignore
            email=random.choice(emails),  # type: ignore
            message=random.choice(sample_messages),  # type: ignore
            date_created=created_date,  # type: ignore
            status=random.choice(statuses),  # type: ignore
        )
        messages.append(message)

    return messages


def main():
    print("Creating database with mock data...")

    os.environ["FLASK_CONFIG"] = "development"

    app = create_app("development")

    print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")

    with app.app_context():
        print("Dropping existing tables...")
        db.drop_all()

        print("Creating tables...")
        db.create_all()

        print("Generating mock messages...")
        mock_messages = create_mock_data()

        print("Inserting mock data...")
        for message in mock_messages:
            db.session.add(message)

        db.session.commit()

        message_count = Message.query.count()
        print(f"Database created successfully!")
        print(f"{message_count} mock messages inserted.")

        print("\nSample messages:")
        sample_messages = Message.query.limit(5).all()
        for msg in sample_messages:
            print(f"  ID: {msg.id}, Status: {msg.status}")
            print(f"  Message: {msg.message[:50]}...")
            print(f"  Created: {msg.date_created}")
            print("  " + "-" * 50)


if __name__ == "__main__":
    main()
