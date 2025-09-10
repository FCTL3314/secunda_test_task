from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.core import settings

async_engine = create_async_engine(settings.db.url)
async_session_factory = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session
