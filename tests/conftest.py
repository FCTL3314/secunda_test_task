from typing import AsyncGenerator

import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool

from src.core import settings
from src.db.database import get_async_db
from src.db.models import Base
from src.main import app

DATABASE_URL_TEST = "sqlite+aiosqlite:///:memory:"
engine_test = create_async_engine(DATABASE_URL_TEST, poolclass=NullPool)
async_session_maker = async_sessionmaker(engine_test, expire_on_commit=False)


@pytest_asyncio.fixture(scope="function", autouse=True)
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

        await conn.execute(text("""
                                INSERT INTO buildings (id, address, latitude, longitude)
                                VALUES (1, 'г. Москва, ул. Ленина 1, офис 3', 55.7558, 37.6173),
                                       (2, 'г. Новосибирск, ул. Блюхера, 32/1', 55.0084, 82.9357);
                                """))
        await conn.execute(text("""
                                INSERT INTO activities (id, name, parent_id)
                                VALUES (1, 'Еда', NULL),
                                       (2, 'Мясная продукция', 1),
                                       (3, 'Молочная продукция', 1),
                                       (4, 'Автомобили', NULL),
                                       (5, 'Грузовые', 4),
                                       (6, 'Легковые', 4),
                                       (7, 'Запчасти', 6),
                                       (8, 'Аксессуары', 6);
                                """))
        await conn.execute(text("""
                                INSERT INTO organizations (id, name, building_id)
                                VALUES (1, 'ООО "Рога и Копыта"', 1),
                                       (2, 'ПАО "Мясокомбинат"', 2),
                                       (3, 'Молочный завод "Зорька"', 2);
                                """))
        await conn.execute(text("""
                                INSERT INTO phone_numbers (id, number, organization_id)
                                VALUES (1, '2-222-222', 1),
                                       (2, '3-333-333', 1),
                                       (3, '8-923-666-13-13', 2);
                                """))
        await conn.execute(text("""
                                INSERT INTO organization_activity (organization_id, activity_id)
                                VALUES (1, 3),
                                       (2, 2),
                                       (3, 3);
                                """))

    yield

    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def override_get_async_db() -> AsyncGenerator:
    async with async_session_maker() as session:
        yield session


app.dependency_overrides[get_async_db] = override_get_async_db  # noqa


@pytest_asyncio.fixture(scope="function")
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(base_url="http://127.0.0.1:8080") as ac:
        yield ac


@pytest_asyncio.fixture(scope="function")
async def headers() -> dict[str, str]:
    return {"X-API-KEY": settings.api.static_api_key}
