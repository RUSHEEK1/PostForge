"""add user table

Revision ID: d2f1128f4090
Revises: d32f03a387b3
Create Date: 2026-09-29 14:15:50.538614

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd2f1128f4090'
down_revision: Union[str, Sequence[str], None] = 'd32f03a387b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column("created_at",sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )

    pass    


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
    pass
