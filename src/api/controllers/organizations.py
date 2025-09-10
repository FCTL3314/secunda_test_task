from http import HTTPStatus
from typing import Sequence

from fastapi import APIRouter, Depends, HTTPException

from src.api.schemas import Organization
from src.api.controllers.dependencies import get_directory_service
from src.services.directory import DirectoryService

router: APIRouter = APIRouter(
    prefix="/organizations",
    tags=["Organizations"],
)


@router.get(
    "/{organization_id}",
    response_model=Organization,
    summary="Get organization by ID",
)
async def read_organization(
    organization_id: int, service: DirectoryService = Depends(get_directory_service)
) -> Organization:
    db_organization = await service.get_organization_by_id(organization_id)
    if db_organization is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Organization not found")
    return db_organization


@router.get(
    "/",
    response_model=list[Organization],
    summary="Search organizations by name",
)
async def search_organizations_by_name(
    name: str, service: DirectoryService = Depends(get_directory_service)
) -> Sequence[Organization]:
    return await service.search_organizations_by_name(name)


@router.get(
    "/search-by-location/",
    response_model=list[Organization],
    summary="Search organizations by location",
)
async def search_organizations_by_location(
    lat: float,
    lon: float,
    radius: float | None = None,
    min_lat: float | None = None,
    min_lon: float | None = None,
    max_lat: float | None = None,
    max_lon: float | None = None,
    service: DirectoryService = Depends(get_directory_service),
) -> Sequence[Organization]:
    if radius:
        return await service.get_organizations_in_radius(lat, lon, radius)
    elif all([min_lat, min_lon, max_lat, max_lon]):
        return await service.get_organizations_in_bbox(min_lat, min_lon, max_lat, max_lon)
    else:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Either 'radius' or 'min_lat, min_lon, max_lat, max_lon' must be provided.",
        )
