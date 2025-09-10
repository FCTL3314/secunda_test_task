from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from src.db.models import Base


class Building(Base):
    __tablename__ = "buildings"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    organizations = relationship("Organization", back_populates="building")
