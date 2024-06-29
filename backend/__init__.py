import os
from flask import Flask
from . import db
from . import routes

def create_app():
    app = Flask(__name__)

    # Configuration settings
    app.config.from_mapping(
        SECRET_KEY='bruhlmao',
        DATABASE=os.path.join('/home/torment/development/database.db'), # List the path for the database
        USE_API=False # This flag controls the usage of the API, which is currently false since we want to use a local database
    )

    # Initialize database commands
    db.init_app(app)

    # Register routes
    from . import routes
    app.register_blueprint(routes.bp)

    return app