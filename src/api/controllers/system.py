import logging
from http import HTTPStatus

from fastapi import APIRouter, Depends, status
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from src.api.schemas import HealthCheckResponse
from src.db.database import get_async_db

logger = logging.getLogger(__name__)
router = APIRouter(tags=["System"])


@router.get(
    "/health-check",
    response_model=HealthCheckResponse,
    summary="Checking the service status",
    responses={
        status.HTTP_503_SERVICE_UNAVAILABLE: {
            "description": "The service is not available, the error of connecting to the database"
        }
    },
)
async def health_check(
        session: AsyncSession = Depends(get_async_db),
) -> HealthCheckResponse | JSONResponse:
    try:
        await session.execute(text("SELECT 1"))
        return HealthCheckResponse(status="ok", db_connection=True)
    except SQLAlchemyError as e:
        logger.error(
            f"Error connection to the database when checking the condition: {e}"
        )
        return JSONResponse(
            content=HealthCheckResponse(
                status="error", db_connection=False
            ).model_dump(),
            status_code=HTTPStatus.SERVICE_UNAVAILABLE,
        )
