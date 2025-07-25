from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime)
    is_active = Column(Boolean, default=True)
    # role_id = Column(ForeignKey("roles.id"))

    posts = relationship("Post", back_populates="author")
    # comments = relationship("Comment", back_populates="author")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, max_length=255)
    full_text = Column(Text)
    likes = Column(Integer, default=0)
    dislikes = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    author_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True)

    author = relationship("User", back_populates="posts")
    # comments = relationship("Comment", back_populates="post", lazy="select")



class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    likes = Column(Integer)
    created_at = Column(DateTime)
    author_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))

    # author = relationship("User", back_populates="comments")
    # post = relationship("Post", back_populates="comments")