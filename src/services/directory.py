from math import radians, sin, cos, sqrt, atan2
from typing import Sequence

from src.db import models
from src.repositories.directory import DirectoryRepository


def _haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R: float = 6371  # Radius of Earth in kilometers
    lat1_rad, lon1_rad, lat2_rad, lon2_rad = map(radians, [lat1, lon1, lat2, lon2])

    dlon: float = lon2_rad - lon1_rad
    dlat: float = lat2_rad - lat1_rad

    a: float = sin(dlat / 2) ** 2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2) ** 2
    c: float = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


class DirectoryService:
    repository: DirectoryRepository

    def __init__(self, repository: DirectoryRepository) -> None:
        self.repository = repository

    async def get_organization_by_id(self, organization_id: int) -> models.Organization | None:
        return await self.repository.get_organization_by_id(organization_id)

    async def get_all_buildings(self, skip: int = 0, limit: int = 100) -> Sequence[models.Building]:
        return await self.repository.get_all_buildings(skip, limit)

    async def search_organizations_by_name(self, name: str) -> Sequence[models.Organization]:
        return await self.repository.search_organizations_by_name(name)

    async def get_organizations_by_building_id(self, building_id: int) -> Sequence[models.Organization]:
        return await self.repository.get_organizations_by_building_id(building_id)

    async def get_organizations_by_activity(self, activity_id: int) -> Sequence[models.Organization]:
        activity_ids: set[int] = await self.repository.get_all_child_activity_ids(activity_id)
        activity_ids.add(activity_id)
        return await self.repository.get_organizations_by_activity_ids(activity_ids)

    async def search_organizations_by_activity_name(self, name: str) -> Sequence[models.Organization]:
        root_activity: models.Activity | None = await self.repository.find_activity_by_name(name)
        if not root_activity:
            return []

        activity_ids: set[int] = await self.repository.get_all_child_activity_ids(root_activity.id)
        activity_ids.add(root_activity.id)
        return await self.repository.get_organizations_by_activity_ids(activity_ids)

    async def get_organizations_in_radius(self, lat: float, lon: float, radius: float) -> Sequence[models.Organization]:
        all_buildings: Sequence[models.Building] = await self.repository.get_all_buildings(limit=1000)
        building_ids_in_radius: list[int] = [
            building.id
            for building in all_buildings
            if _haversine_distance(lat, lon, building.latitude, building.longitude) <= radius
        ]
        return await self.repository.get_organizations_by_building_ids(building_ids_in_radius)

    async def get_organizations_in_bbox(
        self, min_lat: float, min_lon: float, max_lat: float, max_lon: float
    ) -> Sequence[models.Organization]:
        return await self.repository.get_organizations_in_bbox(min_lat, min_lon, max_lat, max_lon)
