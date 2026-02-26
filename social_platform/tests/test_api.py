import requests

BASE_URL = "http://127.0.0.1:8000/api"

# -- test user
print("\n=== Creating Users ===")
users = [
    {
        "username": "Charles",
        "email": "charles@example.com",
        "bio": "I want to be a real boy!",
    },
    {
        "username": "Jennifer",
        "email": "jennifer@example.com",
        "bio": "Wife, mother, friend!",
    },
]
for user in users:
    response = requests.post(f"{BASE_URL}/users", json=user)
    print(
        f"POST /users {user['username']} ->",
        response.status_code,
        response.json() if response.content else "",
    )

# --- test posts
print("\n--- creating posts ---")
posts = [
    {"author": "Charles", "content": "Hey all! This is a cool app!"},
    {"author": "Jennifer", "content": "I don't know if anyone can see this, but HI!"},
    {
        "author": "Charles",
        "content": "Man, things have gotten pretty strange around here!",
    },
]

for post in posts:
    response = requests.post(f"{BASE_URL}/posts", json=post)
    print(
        f"POST /posts {post['author']} ->",
        response.status_code,
        response.json() if response.content else "",
    )

# --- test following
print("\n--- following users ---")
follows = [
    {"follower": "Charles", "following": "Jennifer"},
    {"follower": "Jennifer", "following": "Charles"},
]
for f in follows:
    response = requests.post(f"{BASE_URL}/follow/{f['follower']}/{f['following']}")
    print(
        f"POST /follow {f['follower']} -> {f['following']} ->",
        response.status_code,
        response.json() if response.content else "",
    )

# --- test feeds
print("\n--- fetching feeds ---")
for user in ["Charles", "Jennifer"]:
    response = requests.get(f"{BASE_URL}/feed/{user}")
    print(f"GET /feed/{user} ->", response.status_code)
    print(response.json() if response.content else "No posts")

# --- done
print("\n--- api test complete ---")
