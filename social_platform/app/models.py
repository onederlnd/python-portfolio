# models.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# --- user model
class User(BaseModel):
    username: str
    email: str
    bio: Optional[str] = None


class Post(BaseModel):
    author: str
    content: str
    timestamp: Optional[datetime] = None


# -- follow model
class Follow(BaseModel):
    follower: str  # username
    following: str  # username
