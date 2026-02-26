# Social Media Platform

A simple full-stack social media app built with FastAPI (backend) and vanilla JavaScript (frontend). Users can create accounts, post updates, follow each other, and view a feed of posts from themselves and those they follow.

---

## Features

- User accounts: Create a username, email, and bio.  
- Posts: Users can write posts.  
- Follow system: Follow and be followed by other users.  
- Feed: View posts from yourself and users you follow.  
- REST API: All functionality available via HTTP endpoints.  
- Frontend: Simple HTML/JS interface for interacting with the API.  

---

## Project Structure

social-platform/
│
├─ app/
│   ├─ main.py          # FastAPI entry point
│   ├─ models.py        # Pydantic models (User, Post)
│   ├─ storage.py       # In-memory storage functions
│   └─ routes.py        # API routes
│
├─ frontend/
│   ├─ index.html       # Frontend interface
│   └─ script.js        # Frontend logic (fetch API calls)
│
└─ README.md

---

## Installation

1. Clone the repository:

git clone https://github.com/onederlnd/python-portfolio.git

cd social-platform

2. Create a virtual environment and activate it:

python -m venv .venv  
source .venv/bin/activate   # Linux/macOS  
.venv\Scripts\activate      # Windows  

3. Install dependencies:

pip install fastapi uvicorn

---

## Running the Backend

Start the FastAPI server:

uvicorn app.main:app --reload

The API will run at: http://127.0.0.1:8000

You can also open the auto-generated docs at: http://127.0.0.1:8000/docs

---

## Running the Frontend

1. Open frontend/index.html in your browser.  
2. The frontend communicates with the backend API at http://127.0.0.1:8000.  
3. Use the interface to:  
   - Create users  
   - Make posts  
   - Follow other users  
   - View feeds  

---

## API Endpoints

Method | Endpoint | Description  
--- | --- | ---  
POST | /api/users | Create a new user  
POST | /api/posts | Create a new post  
GET  | /api/feed/{username} | Get the feed for a user  
POST | /api/follow/{follower}/{following} | Follower follows another user  

---

## Example Usage

Create users:  
POST /api/users {"username": "Charles", "email": "charles@example.com", "bio": "I want to be a real boy!"}  
POST /api/users {"username": "Jennifer", "email": "jennifer@example.com", "bio": "Wife, mother, friend!"}

Create posts:  
POST /api/posts {"author": "Charles", "content": "Hey all! This is a cool app!"}  
POST /api/posts {"author": "Jennifer", "content": "I don't know if anyone can see this, but HI!"}  
POST /api/posts {"author": "Charles", "content": "Man, things have gotten pretty strange around here!"}

Follow users:  
POST /api/follow/Charles/Jennifer  
POST /api/follow/Jennifer/Charles

Get feed:  
GET /api/feed/Charles  
GET /api/feed/Jennifer

---

## Notes

- Data is currently stored in-memory. Restarting the server will clear all users and posts.  
- Designed for educational purposes and to demonstrate full-stack development skills.  

---

## Future Improvements

- Add persistent storage with SQLite or PostgreSQL.  
- Add authentication (JWT tokens or OAuth2).  
- Style the frontend with CSS frameworks (Bootstrap, Tailwind).  
- Add post likes, comments, and notifications.  

---

## License

MIT License