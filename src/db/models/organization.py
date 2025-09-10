from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from src.db.models import Base

organization_activity_association = Table(
    "organization_activity",
    Base.metadata,
    Column("organization_id", Integer, ForeignKey("organizations.id"), primary_key=True),
    Column("activity_id", Integer, ForeignKey("activities.id"), primary_key=True),
)


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    building_id = Column(Integer, ForeignKey("buildings.id"))

    building = relationship("Building", back_populates="organizations")
    phone_numbers = relationship("PhoneNumber", back_populates="organization")
    activities = relationship(
        "Activity",
        secondary=organization_activity_association,
        back_populates="organizations",
    )
