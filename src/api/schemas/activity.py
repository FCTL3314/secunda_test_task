from pydantic import BaseModel


class ActivityBase(BaseModel):
    name: str


class Activity(ActivityBase):
    id: int
    parent_id: int | None = None

    class Config:
        from_attributes = True
