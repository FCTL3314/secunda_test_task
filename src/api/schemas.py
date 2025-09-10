from typing import Literal

from pydantic import BaseModel


class PhoneNumberBase(BaseModel):
    number: str


class PhoneNumber(PhoneNumberBase):
    id: int
    organization_id: int

    class Config:
        from_attributes = True


class ActivityBase(BaseModel):
    name: str


class Activity(ActivityBase):
    id: int
    parent_id: int | None = None

    class Config:
        from_attributes = True


class BuildingBase(BaseModel):
    address: str
    latitude: float
    longitude: float


class Building(BuildingBase):
    id: int

    class Config:
        from_attributes = True


class OrganizationBase(BaseModel):
    name: str


class Organization(OrganizationBase):
    id: int
    building: Building
    phone_numbers: list[PhoneNumber] = []
    activities: list[Activity] = []

    class Config:
        from_attributes = True


class HealthCheckResponse(BaseModel):
    status: Literal["ok", "error"]
    db_connection: bool
