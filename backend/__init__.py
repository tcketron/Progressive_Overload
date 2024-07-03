from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS for all routes
    
    app.config['DATABASE'] = '../database.db'  # Update the path accordingly
    
    with app.app_context():
        from . import db
        db.init_app(app)
    
    from . import routes
    app.register_blueprint(routes.bp)
    
    return app
