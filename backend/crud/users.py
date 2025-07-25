from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.blog import User
from schemas.users import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def get_user(db: AsyncSession, username: str):
    result = await db.execute(select(User).where(User.username == username))
    return result.scalars().first()


async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()


async def create_user(db: AsyncSession, user: UserCreate):
    hashed_password = pwd_context.hash(user.password1)
    db_user = User(
        email=user.email,
        username=user.username,
        name=user.name,
        surname=user.surname,
        hashed_password=hashed_password,
        created_at=datetime.now()
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user