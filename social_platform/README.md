Social Media API

A Twitter-style social media API built with FastAPI. Users can create accounts, make posts, follow other users, and view their feed.

Features

Create users with username and bio

Make posts with timestamp

Follow other users

Fetch feed (posts by users you follow)

Simple in-memory storage (replaceable with a database)

Installation

Clone the repository:

git clone <your-repo-url>
cd social-media-api

Create a virtual environment and activate it:

python3 -m venv .venv
source .venv/bin/activate # Linux/Mac
.venv\Scripts\activate # Windows

Install dependencies:

pip install fastapi uvicorn

Run the API
uvicorn app.main:app --reload

Open your browser or API client at: http://127.0.0.1:8000/docs

/docs provides an interactive Swagger UI for testing all endpoints.

API Endpoints
Users

POST /api/users — create a new user

Body example:

{
"username": "johndoe",
"email": "john@example.com
",
"bio": "Hello world!"
}

Posts

POST /api/posts — create a new post

Body example:

{
"author": "johndoe",
"content": "This is my first post!"
}

Feed

GET /api/feed/{username} — fetch posts from users you follow

Follow

POST /api/follow/{follower}/{following} — follow another user

Storage

Currently uses in-memory dictionaries. Perfect for testing and demos. You can replace with SQLite or PostgreSQL later.