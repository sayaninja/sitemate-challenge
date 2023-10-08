# Issues API

This repository contains a simple RESTful API for managing issues, similar to platforms like GitHub or Jira. The API allows clients to Create, Read, Update, and Delete issues. Each issue has an `id`, `title`, and `description`.

The project is built using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python.

## Prerequisites

- Python 3.8 or newer
- FastAPI
- Uvicorn (for serving the application)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/<your-username>/sitemate-challenge.git
   cd sitemate-challenge
   ```

2. (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
   ```

3. Install the required packages:

   ```bash
   pip install fastapi uvicorn
   ```

## Running the Server

To run the FastAPI application:

```bash
uvicorn server:app --reload
```

This will start the server on `http://localhost:8000`.

## API Documentation

Once the server is running, you can navigate to `http://localhost:8000/docs` in your web browser to access the Swagger UI, which provides a user-friendly interface to view and test the API endpoints.

## Endpoints

- **Create Issue**:
    - Method: `POST`
    - Endpoint: `/issues/`
    - Body: `{ "title": "<title>", "description": "<description>" }`

- **Read Issues**:
    - Method: `GET`
    - Endpoint: `/issues/`

- **Update Issue**:
    - Method: `PUT`
    - Endpoint: `/issues/{issue_id}`
    - Body: `{ "title": "<title>", "description": "<description>" }`

- **Delete Issue**:
    - Method: `DELETE`
    - Endpoint: `/issues/{issue_id}`

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.
