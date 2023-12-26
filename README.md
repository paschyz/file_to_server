# Document Upload Server

This project is a simple Flask application that provides an endpoint for uploading documents to a server. It can be used to test the functionality of automatically sending documents to a server using a Python script. It watches a specified folder then sends what's added in that specific folder then sends a request that contains the new file to a server.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Python 3.x
- Flask 

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/document-upload-server.git

1. Navigate to the project directory:
   ```bash
   cd document-upload-server

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

### Usage

1. Run the Flask application:
   ```bash
   python app.py

The server will start on http://127.0.0.1:5000/.

2. Use a tool like curl or Postman to simulate file uploads:
   ```bash
   curl -X POST -F "file=@/path/to/your/document.pdf" http://localhost:5000/upload
   
### Project Structure

- main.py: The main file watcher and request 
  
- app.py: The main Flask application.
  
- uploads/: Directory where uploaded files are stored.
