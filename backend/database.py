from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base




SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///blog.db"

async_engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True
)


AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


Base = declarative_base()


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session