from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.db.models.base import Base

if TYPE_CHECKING:
    from src.db.models.organization import Organization


class PhoneNumber(Base):
    __tablename__ = "phone_numbers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    number: Mapped[str] = mapped_column(String(50))
    organization_id: Mapped[int] = mapped_column(Integer, ForeignKey("organizations.id"))

    organization: Mapped["Organization"] = relationship(back_populates="phone_numbers")
