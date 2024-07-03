from flask import Blueprint, jsonify, send_from_directory, request
from flask_cors import CORS
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

DATABASE = '../database.db'

@bp.route('/api/<table>', methods=['GET'])
def get_data(table):
    db = get_db()
    cur = db.cursor()
    cur.execute(f'SELECT * FROM {table}')
    rows = cur.fetchall()
    return jsonify([dict(row) for row in rows])

@bp.route('/api/<table>', methods=['POST'])
def add_row(table):
    data = request.get_json()
    db = get_db()
    columns = ', '.join(data.keys())
    placeholders = ', '.join('?' * len(data))
    query = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
    db.execute(query, list(data.values()))
    db.commit()
    return jsonify({'status': 'success'}), 201