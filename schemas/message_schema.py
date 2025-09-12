from marshmallow import Schema, fields, validate


class MessageSchema(Schema):
    email = fields.Email(required=True)
    subject = fields.Str(required=True, validate=validate.Length(min=1, max=255))
    message = fields.Str(required=True, validate=validate.Length(min=1, max=1000))
