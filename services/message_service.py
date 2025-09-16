import bleach
from exceptions.exceptions import NotFoundException, DuplicateException
from models.message_model import Message
from repositories.message_repository import Messages


class MessageService:
    def __init__(self, *args, **kwargs):
        self.message_repository = Messages()

    def get_all(self):
        return self.message_repository.get_all_sorted_by_date()

    def get_by_id(self, id):
        message = self.message_repository.get_by_id(id)
        if not message:
            raise NotFoundException(f"Message {id} not found")
        return message

    def create(self, message_item):
        if self.message_repository.filter_by(
            email=message_item["email"], message=message_item["message"]
        ):
            raise DuplicateException("Duplicate message detected")

        sanitized_message = bleach.clean(message_item["message"], strip=True)

        new_message = Message()
        new_message.email = message_item["email"]
        new_message.subject = message_item["subject"]
        new_message.message = sanitized_message

        return self.message_repository.create(new_message)

    def update(self, id, **kwargs):
        message = self.get_by_id(id)
        # Only allow status to be 'open' or 'closed'
        if "status" in kwargs:
            status = kwargs["status"]
            if status not in ["open", "closed"]:
                raise ValueError("Status must be 'open' or 'closed'.")
            message.status = status
        self.message_repository.update(message)
        return message
