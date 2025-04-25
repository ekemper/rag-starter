from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'data/docs'
ALLOWED_EXTENSIONS = {'txt'}

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if a file was sent in the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    
    # Check if a file was selected
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    # Check if the file is allowed
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed. Only .txt files are accepted'}), 400
    
    # Secure the filename and save the file
    filename = secure_filename(file.filename)
    try:
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return jsonify({
            'message': 'File uploaded successfully',
            'filename': filename
        }), 201
    except Exception as e:
        return jsonify({'error': f'Error saving file: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001) 