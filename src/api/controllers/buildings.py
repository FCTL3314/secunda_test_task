from typing import Sequence

from fastapi import APIRouter, Depends

from src.api.schemas import Building, Organization
from src.api.controllers.dependencies import get_directory_service
from src.services.directory import DirectoryService

router: APIRouter = APIRouter(
    prefix="/buildings",
    tags=["Buildings"],
)


@router.get(
    "/",
    response_model=list[Building],
    summary="Get all buildings",
)
async def read_buildings(
    skip: int = 0,
    limit: int = 100,
    service: DirectoryService = Depends(get_directory_service),
) -> Sequence[Building]:
    return await service.get_all_buildings(skip, limit)


@router.get(
    "/{building_id}/organizations",
    response_model=list[Organization],
    summary="Get organizations in a specific building",
)
async def read_organizations_in_building(
    building_id: int, service: DirectoryService = Depends(get_directory_service)
) -> Sequence[Organization]:
    return await service.get_organizations_by_building_id(building_id)
