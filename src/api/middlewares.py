from http import HTTPStatus

from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader

from src.core.config import settings

API_KEY_NAME: str = "X-API-KEY"
api_key_header: APIKeyHeader = APIKeyHeader(name=API_KEY_NAME, auto_error=True)


def verify_api_key(api_key: str = Security(api_key_header)) -> str:
    if api_key != settings.api.static_api_key:
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN, detail="Could not validate credentials")
    return api_key
