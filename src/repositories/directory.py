from typing import Sequence

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.db import models


class DirectoryRepository:
    db: AsyncSession

    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_organization_by_id(self, organization_id: int) -> models.Organization | None:
        query = (
            select(models.Organization)
            .options(
                joinedload(models.Organization.phone_numbers),
                joinedload(models.Organization.activities),
                joinedload(models.Organization.building),
            )
            .where(models.Organization.id == organization_id)
        )
        result = await self.db.execute(query)
        return result.scalars().first()

    async def get_all_buildings(self, skip: int = 0, limit: int = 100) -> Sequence[models.Building]:
        query = select(models.Building).offset(skip).limit(limit)
        result = await self.db.execute(query)
        return result.scalars().all()

    async def search_organizations_by_name(self, name: str) -> Sequence[models.Organization]:
        query = (
            select(models.Organization)
            .where(models.Organization.name.ilike(f"%{name}%"))
            .options(
                joinedload(models.Organization.phone_numbers),
                joinedload(models.Organization.activities),
                joinedload(models.Organization.building),
            )
        )
        result = await self.db.execute(query)
        return result.scalars().unique().all()

    async def get_organizations_by_building_id(self, building_id: int) -> Sequence[models.Organization]:
        query = (
            select(models.Organization)
            .where(models.Organization.building_id == building_id)
            .options(
                joinedload(models.Organization.phone_numbers),
                joinedload(models.Organization.activities),
                joinedload(models.Organization.building),
            )
        )
        result = await self.db.execute(query)
        return result.scalars().unique().all()

    async def get_all_child_activity_ids(self, activity_id: int) -> set[int]:
        query = select(models.Activity.id).where(models.Activity.parent_id == activity_id)
        result = await self.db.execute(query)
        child_ids: set[int] = set(result.scalars().all())
        all_child_ids: set[int] = set(child_ids)

        for child_id in child_ids:
            all_child_ids.update(await self.get_all_child_activity_ids(child_id))

        return all_child_ids

    async def get_organizations_by_activity_ids(self, activity_ids: set[int]) -> Sequence[models.Organization]:
        query = (
            select(models.Organization)
            .join(models.organization_activity_association)
            .where(models.organization_activity_association.c.activity_id.in_(activity_ids))
            .options(
                joinedload(models.Organization.phone_numbers),
                joinedload(models.Organization.activities),
                joinedload(models.Organization.building),
            )
            .distinct()
        )
        result = await self.db.execute(query)
        return result.scalars().unique().all()

    async def get_organizations_by_building_ids(self, building_ids: list[int]) -> Sequence[models.Organization]:
        if not building_ids:
            return []
        query = (
            select(models.Organization)
            .where(models.Organization.building_id.in_(building_ids))
            .options(
                joinedload(models.Organization.phone_numbers),
                joinedload(models.Organization.activities),
                joinedload(models.Organization.building),
            )
        )
        result = await self.db.execute(query)
        return result.scalars().unique().all()

    async def get_organizations_in_bbox(
        self, min_lat: float, min_lon: float, max_lat: float, max_lon: float
    ) -> Sequence[models.Organization]:
        building_ids_subquery = (
            select(models.Building.id)
            .where(
                models.Building.latitude.between(min_lat, max_lat),
                models.Building.longitude.between(min_lon, max_lon),
            )
        )
        query = (
            select(models.Organization)
            .where(models.Organization.building_id.in_(building_ids_subquery))
            .options(
                joinedload(models.Organization.phone_numbers),
                joinedload(models.Organization.activities),
                joinedload(models.Organization.building),
            )
        )
        result = await self.db.execute(query)
        return result.scalars().unique().all()

    async def find_activity_by_name(self, name: str) -> models.Activity | None:
        query = select(models.Activity).where(models.Activity.name.ilike(f"%{name}%"))
        result = await self.db.execute(query)
        return result.scalars().first()
