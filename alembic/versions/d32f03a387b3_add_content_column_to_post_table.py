"""add content column to post table

Revision ID: d32f03a387b3
Revises: 128124c09148
Create Date: 2026-09-29 14:07:09.618161

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd32f03a387b3'
down_revision: Union[str, Sequence[str], None] = '128124c09148'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
