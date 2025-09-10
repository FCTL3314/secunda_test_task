"""seed_initial_data

Revision ID: 224db96f8c65
Revises: 6d2d0ff6662e
Create Date: 2025-09-10 08:53:05.233181

"""
from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '224db96f8c65'
down_revision: Union[str, Sequence[str], None] = '6d2d0ff6662e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Buildings
    op.execute(
        """
        INSERT INTO buildings (id, address, latitude, longitude)
        VALUES (1, 'г. Москва, ул. Ленина 1, офис 3', 55.7558, 37.6173),
               (2, 'г. Новосибирск, ул. Блюхера, 32/1', 55.0084, 82.9357);
        """
    )
    op.execute("SELECT setval('buildings_id_seq', (SELECT MAX(id) FROM buildings));")

    # Activities
    op.execute(
        """
        INSERT INTO activities (id, name, parent_id)
        VALUES (1, 'Еда', NULL),
               (2, 'Мясная продукция', 1),
               (3, 'Молочная продукция', 1),
               (4, 'Автомобили', NULL),
               (5, 'Грузовые', 4),
               (6, 'Легковые', 4),
               (7, 'Запчасти', 6),
               (8, 'Аксессуары', 6);
        """
    )
    op.execute("SELECT setval('activities_id_seq', (SELECT MAX(id) FROM activities));")

    # Organizations
    op.execute(
        """
        INSERT INTO organizations (id, name, building_id)
        VALUES (1, 'ООО "Рога и Копыта"', 1),
               (2, 'ПАО "Мясокомбинат"', 2),
               (3, 'Молочный завод "Зорька"', 2);
        """
    )
    op.execute("SELECT setval('organizations_id_seq', (SELECT MAX(id) FROM organizations));")

    # Phone Numbers
    op.execute(
        """
        INSERT INTO phone_numbers (id, number, organization_id)
        VALUES (1, '2-222-222', 1),
               (2, '3-333-333', 1),
               (3, '8-923-666-13-13', 2);
        """
    )
    op.execute("SELECT setval('phone_numbers_id_seq', (SELECT MAX(id) FROM phone_numbers));")

    # Organization activity associations
    op.execute(
        """
        INSERT INTO organization_activity (organization_id, activity_id)
        VALUES (1, 3),
               (2, 2),
               (3, 3);
        """
    )


def downgrade() -> None:
    op.execute(
        "TRUNCATE TABLE organization_activity, phone_numbers, organizations, activities, buildings RESTART IDENTITY CASCADE;")
