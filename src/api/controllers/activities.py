from typing import Sequence

from fastapi import APIRouter, Depends

from src.api import schemas
from src.api.controllers.dependencies import get_directory_service
from src.services.directory import DirectoryService

router: APIRouter = APIRouter(
    prefix="/activities",
    tags=["Activities"],
)


@router.get(
    "/{activity_id}/organizations",
    response_model=list[schemas.Organization],
    summary="Get organizations by activity (including sub-activities)",
)
async def read_organizations_by_activity(
    activity_id: int, service: DirectoryService = Depends(get_directory_service)
) -> Sequence[schemas.Organization]:
    return await service.get_organizations_by_activity(activity_id)


@router.get(
    "/search/",
    response_model=list[schemas.Organization],
    summary="Search organizations by activity name (including sub-activities)",
)
async def search_organizations_by_activity_name(
    name: str, service: DirectoryService = Depends(get_directory_service)
) -> Sequence[schemas.Organization]:
    return await service.search_organizations_by_activity_name(name)
