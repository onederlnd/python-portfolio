from app.models import User, Post, Follow
from typing import Dict, List
from datetime import datetime

# --- in-memory storage
users: Dict[str, User] = {}
posts: Dict[str, User] = {}
follows: List[Follow] = []


# --- create user
def create_user(user: User):
    users[user.username] = user
    return user


# --- create post
def create_post(post: Post):
    post.timestamp = datetime.now()
    post_id = len(posts) + 1
    posts[str(post_id)] = post
    return post_id


# --- get feed for a user
def get_feed(username: str):
    following = [f.following for f in follows if f.follower == username]
    feed_posts = [
        p for p in posts.values() if p.author in following or p.author == username
    ]
    # sort by timestamp descending
    feed_posts.sort(key=lambda x: x.timestamp, reverse=True)
    return feed_posts


# --- follow user
def add_follow(follower: str, following: str):
    follows.append(Follow(follower=follower, following=following))
    return True
