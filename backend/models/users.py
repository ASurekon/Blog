from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base
from .blog import Post


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
    comments = relationship("Comment", back_populates="author")



# class Role(Base):
#     __tablename__ = "roles"

#     id = Column(Integer)
#     role_name = Column(String)