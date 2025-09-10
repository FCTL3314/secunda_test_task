from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.db.models.base import Base

if TYPE_CHECKING:
    from src.db.models.organization import Organization


class Activity(Base):
    __tablename__ = "activities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), index=True)
    parent_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("activities.id"), nullable=True)

    parent: Mapped[Optional["Activity"]] = relationship(remote_side=[id], back_populates="children")
    children: Mapped[List["Activity"]] = relationship(back_populates="parent")
    organizations: Mapped[List["Organization"]] = relationship(
        secondary="organization_activity",
        back_populates="activities",
    )
