from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
    AsyncEngine,
)

from src.core.config import settings

async_engine: AsyncEngine = create_async_engine(settings.db.url)
async_session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
    async_engine, expire_on_commit=False
)


async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session
