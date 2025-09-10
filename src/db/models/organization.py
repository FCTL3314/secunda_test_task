from typing import TYPE_CHECKING, List

from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.db.models.base import Base

if TYPE_CHECKING:
    from src.db.models.building import Building
    from src.db.models.phone_number import PhoneNumber
    from src.db.models.activity import Activity


organization_activity_association: Table = Table(
    "organization_activity",
    Base.metadata,
    Column("organization_id", Integer, ForeignKey("organizations.id"), primary_key=True),
    Column("activity_id", Integer, ForeignKey("activities.id"), primary_key=True),
)


class Organization(Base):
    __tablename__ = "organizations"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), index=True)
    building_id: Mapped[int] = mapped_column(ForeignKey("buildings.id"))

    building: Mapped["Building"] = relationship(back_populates="organizations")
    phone_numbers: Mapped[List["PhoneNumber"]] = relationship(back_populates="organization")
    activities: Mapped[List["Activity"]] = relationship(
        secondary=organization_activity_association,
        back_populates="organizations",
    )
