from sqlalchemy.orm import declarative_base

from src.db.models.activity import Activity
from src.db.models.building import Building
from src.db.models.organization import Organization, organization_activity_association
from src.db.models.phone_number import PhoneNumber

Base = declarative_base()
