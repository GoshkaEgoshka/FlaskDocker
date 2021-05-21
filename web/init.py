"""
    This module for init application
"""
from flask import Flask

from models import db


def create_app():
    """
        Creates app
    """
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    if app.config['INIT_DB']:
        with app.app_context():
            db.create_all()
    return app
