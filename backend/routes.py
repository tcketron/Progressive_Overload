from flask import Blueprint, jsonify, send_from_directory
from .db import get_db

bp = Blueprint('routes', __name__)

# This is the path for our main svelte page
@bp.route('/')
def base():
    return send_from_directory('../frontend/public', 'index.html')

# Path for the static files (Compiled JS/CSS, etc.)
@bp.route("/<path:path>")
def home(path):
    return send_from_directory('../frontend/public', path)

# This path is for the /api/data (currently legs)
@bp.route('/api/data', methods=['GET'])
def get_data():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM legs')
    data = cursor.fetchall()
    return jsonify([dict(row) for row in data]) # Can also just do data
