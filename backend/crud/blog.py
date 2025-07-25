from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.blog import Post, Comment
from schemas.blog import PostCreate, PostUpdate, CommentPost, CommentUpdate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_posts(db: AsyncSession, user_id: int, skip: int = 0, limit: int = 100):
    result = await db.execute(
        select(Post)
        .where(Post.author_id == user_id)
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()


async def create_user_post(db: AsyncSession, post: PostCreate, user_id: int):
    db_post = Post(
        **post.model_dump(),
        author_id=user_id,
        created_at=datetime.now()
    )
    db.add(db_post)
    await db.commit()
    await db.refresh(db_post)
    return db_post


async def get_post(db: AsyncSession, post_id: int, user_id: int):
    result = await db.execute(
        select(Post)
        .where(Post.id == post_id)
        .where(Post.author_id == user_id)
    )
    return result.scalars().first()


async def update_post(db: AsyncSession, db_post: Post, post: PostUpdate):
    update_data = post.model_dump(exclude_defaults=True)
    for field, value in update_data.items():
        setattr(db_post, field, value)
    setattr(db_post, "updated_at", datetime.now())
    db.add(db_post)
    await db.commit()
    await db.refresh(db_post)
    return db_post


async def delete_post(db: AsyncSession, db_post: Post):
    await db.delete(db_post)
    await db.commit()