# RAG Starter API Documentation

## Overview
This API provides endpoints for uploading documents to be processed by the RAG (Retrieval-Augmented Generation) system.

## Setup and Running the API

### Installation
1. Clone the repository and navigate to the project directory

2. Create and activate a virtual environment (recommended):
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the API

#### Production Mode
Start the API server normally:
```bash
python api.py
```

#### Development Mode (with Hot Reload)
For local development with automatic reloading on file changes:

1. Install development dependencies:
```bash
pip install -r requirements.txt
```

2. Run the development server:
```bash
python run_dev.py
```

Features of development mode:
- Automatic server restart when Python files change
- Debug mode enabled
- Detailed error pages
- Real-time code reloading

The server will start on `http://localhost:5001` and automatically restart when you make changes to any Python file in the project.

### Environment Variables
No environment variables are required for basic file upload functionality. However, if you plan to use the RAG features, you'll need:
- `OPENAI_API_KEY`: Your OpenAI API key

### Directory Structure
The API will automatically create required directories:
- `data/docs/`: Where uploaded text files are stored

### Health Check
Once the server is running, you can verify it's working by:
1. Opening a browser to `http://localhost:5001`
2. Using curl:
```bash
curl http://localhost:5001/upload
```
You should receive a 400 response indicating the endpoint is working but requires a file upload.

## Base URL

## Endpoints

### Upload Document
Upload a text file to be processed by the RAG system.

**URL**: `/upload`
**Method**: `POST`
**Content-Type**: `multipart/form-data`

#### Request Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| file | File | Yes | Text file to upload (.txt only) |

#### Responses

##### Success Response
**Code**: `201 CREATED`
```json
{
    "message": "File uploaded successfully",
    "filename": "example.txt"
}
```

##### Error Responses
**Code**: `400 BAD REQUEST`
```json
{
    "error": "No file part in the request"
}
```
OR
```json
{
    "error": "No file selected"
}
```
OR
```json
{
    "error": "File type not allowed. Only .txt files are accepted"
}
```

**Code**: `500 INTERNAL SERVER ERROR`
```json
{
    "error": "Error saving file: [error details]"
}
```

## Example Usage

### Using cURL
```bash
curl -X POST -F "file=@/path/to/your/document.txt" http://localhost:5001/upload
```

### Using Python Requests
```python
import requests

url = 'http://localhost:5001/upload'
files = {'file': open('document.txt', 'rb')}
response = requests.post(url, files=files)
print(response.json())
```

## Running Tests
To run the test suite:

1. Install test dependencies:
```bash
pip install pytest
```

2. Run tests:
```bash
pytest tests/test_api.py -v
```

## Error Handling
- The API only accepts .txt files
- Filenames are sanitized for security
- Empty files or missing files will be rejected
- Server errors during file saving will return appropriate error messages

## Security Considerations
- Filenames are sanitized to prevent directory traversal attacks
- File types are strictly validated
- Upload directory is automatically created if it doesn't exist 