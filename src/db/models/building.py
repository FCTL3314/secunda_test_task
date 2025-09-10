from typing import TYPE_CHECKING, List

from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.db.models.base import Base

if TYPE_CHECKING:
    from src.db.models.organization import Organization


class Building(Base):
    __tablename__ = "buildings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    address: Mapped[str] = mapped_column(String(255))
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)

    organizations: Mapped[List["Organization"]] = relationship(back_populates="building")
