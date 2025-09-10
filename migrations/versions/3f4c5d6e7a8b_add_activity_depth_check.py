"""add_activity_depth_check

Revision ID: 3f4c5d6e7a8b
Revises: 224db96f8c65
Create Date: 2024-05-20 12:00:00.000000

"""
from typing import Sequence, Union

from alembic import op

revision: str = '3f4c5d6e7a8b'
down_revision: Union[str, Sequence[str], None] = '224db96f8c65'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        CREATE
        OR REPLACE FUNCTION get_activity_depth(p_activity_id integer)
        RETURNS integer AS
        $BODY$
        DECLARE
        v_depth integer;
        BEGIN
        WITH RECURSIVE activity_tree AS (SELECT id, parent_id, 1 as depth
                                         FROM activities
                                         WHERE id = p_activity_id
                                         UNION ALL
                                         SELECT a.id, a.parent_id, at.depth + 1
                                         FROM activities a
                                                  JOIN activity_tree at
        ON a.id = at.parent_id
            )
        SELECT max(depth)
        INTO v_depth
        FROM activity_tree;
        RETURN v_depth;
        END;
        $BODY$
        LANGUAGE plpgsql;
        """
    )
    op.execute(
        """
        ALTER TABLE activities
            ADD CONSTRAINT chk_activity_depth CHECK (get_activity_depth(id) <= 3);
        """
    )


def downgrade() -> None:
    op.execute("ALTER TABLE activities DROP CONSTRAINT chk_activity_depth;")
    op.execute("DROP FUNCTION get_activity_depth(integer);")
