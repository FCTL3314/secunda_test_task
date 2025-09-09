from pydantic import BaseModel
from typing import List, Optional


class PhoneNumberBase(BaseModel):
    number: str


class PhoneNumber(PhoneNumberBase):
    id: int
    organization_id: int

    class Config:
        orm_mode = True


class ActivityBase(BaseModel):
    name: str


class Activity(ActivityBase):
    id: int
    parent_id: Optional[int] = None

    class Config:
        orm_mode = True


class BuildingBase(BaseModel):
    address: str
    latitude: float
    longitude: float


class Building(BuildingBase):
    id: int

    class Config:
        orm_mode = True


class OrganizationBase(BaseModel):
    name: str


class Organization(OrganizationBase):
    id: int
    building: Building
    phone_numbers: List[PhoneNumber] = []
    activities: List[Activity] = []

    class Config:
        orm_mode = True
