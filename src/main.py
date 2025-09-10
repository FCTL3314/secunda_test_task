from fastapi import FastAPI

from src.api.handlers.lifespan import lifespan

app: FastAPI = FastAPI(
    title="Directory API",
    description="API for a directory of Organizations, Buildings, and Activities.",
    version="1.0.0",
    lifespan=lifespan,
)
