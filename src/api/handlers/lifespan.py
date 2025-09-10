from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from src.api.controllers import base_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    app.include_router(base_router)
    yield
