"""
    Validation module
"""
import json

from marshmallow import Schema, fields


class UserValidation(Schema):
    """
        Class for validation users data
    """
    user_id = fields.Int(required=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
