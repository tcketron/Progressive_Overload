import os
from flask import Flask, send_from_directory
from . import db, routes

def create_app():
    app = Flask(__name__)

    app.config['DATABASE'] = '../database.db'

    # Register your main routes
    from .routes import bp as blueprint
    app.register_blueprint(blueprint)

    # Initialize database commands
    db.init_app(app)

    # Check and create database if it doesn't exist
    with app.app_context():
        db.check_and_create_db(app)

    return app