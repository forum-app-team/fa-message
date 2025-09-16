from models.message_model import Message, db


class Messages:
    def get_all(self):
        return Message.query.order_by(Message.id.desc()).all()

    def get_all_sorted_by_date(self):
        return Message.query.order_by(Message.date_created.desc()).all()

    def filter_by(self, **kwargs):
        query = Message.query
        if "email" in kwargs:
            query = query.filter(Message.email.like(f"%{kwargs['email']}%"))
        if "subject" in kwargs:
            query = query.filter(Message.subject.like(f"%{kwargs['subject']}%"))
        if "message" in kwargs:
            query = query.filter(Message.message.like(f"%{kwargs['message']}%"))
        return query.all()

    def get_by_id(self, id):
        return db.session.get(Message, id)

    def create(self, message_item):
        db.session.add(message_item)
        db.session.commit()
        return message_item

    def update(self, message_item):
        db.session.add(message_item)
        db.session.commit()
        return message_item
