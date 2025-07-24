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
    comments: int
    owner_id: int
    public_date: datetime
    updated_at: datetime = None



class PostUpdate(BaseModel):
    title: Optional[str] = None
    full_text: Optional[str] = None



class PostResponse(PostCreate):
    pass



class CommentPost(BaseModel):
    test: str


class CommentUpdate(CommentPost):
    pass


class CommentBase(CommentPost):
    id: int
    commentator_id: int
    likes: int
    post_id: int
    commented_at: datetime
    updated_at: datetime