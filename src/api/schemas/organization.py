from pydantic import BaseModel

from src.api.schemas.activity import Activity
from src.api.schemas.building import Building


class PhoneNumberBase(BaseModel):
    number: str


class PhoneNumber(PhoneNumberBase):
    id: int
    organization_id: int

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
