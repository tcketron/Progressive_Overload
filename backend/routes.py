from flask import Blueprint, request, jsonify, current_app, g
from werkzeug.utils import secure_filename
import os
from .db import get_db, close_db, create_custom_table

bp = Blueprint('routes', __name__)

UPLOAD_FOLDER = 'uploads'  # Define upload folder

@bp.route('/upload-table', methods=['POST'])
def upload_table():
    if 'file' not in request.files:
        return jsonify(message="No file part"), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify(message="No selected file"), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.instance_path, UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        # Initialize or create table based on file contents
        create_custom_table(filepath)
        
        return jsonify(message="File uploaded and table created successfully"), 200
    
    return jsonify(message="Invalid file type"), 400

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'db', 'sqlite', 'sqlite3'}

