"""
    Validation module
"""

from marshmallow import Schema, fields, validate


class UserValidation(Schema):
    """
        Class for validation users data
    """
    id = fields.Int(required=True, validate=validate.Range(min=1, max=999999))
    username = fields.Str(required=True, validate=validate.Length(min=2, max=20))
    email = fields.Email(required=True, validate=validate.Length(min=8, max=36))
