from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class PostCreate(BaseModel):
    title: str
    full_text: str



class PostBase(PostCreate):
    id: int
    likes: int
    dislikes: int
    is_active: bool = True
    author_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None



class PostUpdate(BaseModel):
    title: Optional[str] = None
    full_text: Optional[str] = None



class PostResponse(PostBase):
    pass



class CommentPost(BaseModel):
    text: str


class CommentUpdate(CommentPost):
    pass


class CommentBase(CommentPost):
    id: int
    author_id: int
    likes: int
    post_id: int
    created_at: datetime
    # updated_at: datetime