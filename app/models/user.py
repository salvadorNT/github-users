import json
from .core import db
from sqlalchemy import func


class User(db.Model):
    """Model for github user"""
    id = db.Column(db.Integer, primary_key=True, unique=True)
    created_on = db.Column(db.DateTime(), default=func.now())
    username = db.Column(db.String(40), unique=True)
    image_url = db.Column(db.String(256))
    profile_url = db.Column(db.String(256))
    type = db.Column(db.String(16))

    def __init__(self, username, image_url, profile_url, type):
        self.username = username
        self.image_url = image_url
        self.profile_url = profile_url
        self.type = type

    def json(self):
        """method to easily return json list"""
        return {
            'id': self.id,
            'created_on': str(self.created_on),
            'username': self.username,
            'image_url': self.image_url,
            'profile_url': self.profile_url,
            'type': self.type
        }

    @classmethod
    def order_by_id(cls, order=None):
        """Class method to order by id,
        default is ascending if order desc
        does not match"""
        if order == 'desc':
            return cls.query.order_by(cls.id.desc())
        return cls.query.order_by(cls.id.asc())

    @classmethod
    def order_by_username(cls, order=None):
        """Class method to order by username,
        default is ascending if order desc
        does not match"""
        if order == 'desc':
            return cls.query.order_by(cls.username.desc())
        return cls.query.order_by(cls.username.asc())

    def __repr__(self):
        return self.username
