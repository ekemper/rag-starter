# RAG Starter API Documentation

## Overview
This API provides endpoints for uploading documents to be processed by the RAG (Retrieval-Augmented Generation) system.

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
curl -X POST -F "file=@/path/to/your/document.txt" http://localhost:5000/upload
```

### Using Python Requests
```python
import requests

url = 'http://localhost:5000/upload'
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