# Notes API

Simple REST API built using **Python + FastAPI**.

The API supports:

* User login using Basic Authentication
* JWT-based authentication
* Create, read, update and delete notes
* Users can only access their own notes

## Project Structure

```text
notes_application/
├── main.py
├── client.py
├── requirements.txt
└── README.md
```

## Setup

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install fastapi uvicorn pyjwt requests
```

## Run

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Authentication Flow

```text
Basic Auth
    ↓
POST /login
    ↓
JWT token
    ↓
Authorization: Bearer <token>
    ↓
Notes API
```

### Login

Example user:

```text
username: alice
password: password123
```

The client sends Basic Authentication to:

```text
POST /login
```

The API returns:

```json
{
  "access_token": "<JWT>",
  "token_type": "bearer"
}
```

### Get Notes

Use the JWT:

```bash
curl http://127.0.0.1:8000/notes \
  -H "Authorization: Bearer <JWT>"
```

The API gets the `user_id` from the JWT and returns only that user's notes.

## Endpoints

| Method | Endpoint      | Description       |
| ------ | ------------- | ----------------- |
| POST   | `/login`      | Login and get JWT |
| GET    | `/notes`      | Get user's notes  |
| POST   | `/notes`      | Create note       |
| GET    | `/notes/{id}` | Get note          |
| PUT    | `/notes/{id}` | Update note       |
| DELETE | `/notes/{id}` | Delete note       |

## Run Client

With the API running:

```bash
python3 client.py
```

The client logs in, gets the JWT, and uses it to call the Notes API.
