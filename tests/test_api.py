import os
import sys
import pytest
import io

# Add parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_upload_valid_txt_file(client):
    # Create a test file in memory
    data = {'file': (io.BytesIO(b'This is a test file content'), 'test.txt')}
    
    # Make request
    response = client.post('/upload', 
                          content_type='multipart/form-data',
                          data=data)
    
    # Check response
    assert response.status_code == 201
    assert 'test.txt' in response.json['filename']
    
    # Verify file was saved
    assert os.path.exists(os.path.join('data/docs', 'test.txt'))
    
    # Clean up
    os.remove(os.path.join('data/docs', 'test.txt'))

def test_upload_invalid_file_type(client):
    # Try to upload a PDF file
    data = {'file': (io.BytesIO(b'PDF content'), 'test.pdf')}
    
    response = client.post('/upload',
                          content_type='multipart/form-data',
                          data=data)
    
    assert response.status_code == 400
    assert 'File type not allowed' in response.json['error']

def test_upload_no_file(client):
    response = client.post('/upload')
    assert response.status_code == 400
    assert 'No file part in the request' in response.json['error']

def test_upload_empty_filename(client):
    data = {'file': (io.BytesIO(b''), '')}
    response = client.post('/upload',
                          content_type='multipart/form-data',
                          data=data)
    
    assert response.status_code == 400
    assert 'No file selected' in response.json['error'] 