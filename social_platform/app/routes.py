from fastapi import APIRouter, HTTPException
from app.models import User, Post
from app.storage import create_user, create_post, get_feed, add_follow

router = APIRouter(prefix="/api", tags=["social"])


# --- create user
@router.post("/users")
def new_user(user: User):
    if user.username in create_user.__globals__["users"]:
        raise HTTPException(status_code=400, detail="Username already exists")
    return create_user(user)


# --- create post
@router.post("/posts")
def new_post(post: Post):
    return {"post_id": create_post(post)}


# --- get feed
@router.get("/feed/{username}")
def feed(username: str):
    return get_feed(username)


# --- follow user
@router.post("/follow/{follower}/{following}")
def follow_user(follower: str, following: str):
    if (
        follower not in create_user.__globals__["users"]
        or following not in create_user.__globals__["users"]
    ):
        raise HTTPException(status_code=404, detail="User not found")
    add_follow(follower, following)
    return {"detail": f"{follower} now follows {following}"}
