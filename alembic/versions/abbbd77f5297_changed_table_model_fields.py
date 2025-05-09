"""changed table model fields

Revision ID: abbbd77f5297
Revises: 3fd8605a5e7f
Create Date: 2025-05-08 12:53:09.755900

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'abbbd77f5297'
down_revision: Union[str, None] = '3fd8605a5e7f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('fields', sa.Column('mask', sa.String(length=255), nullable=True))
    op.add_column('fields', sa.Column('filter_field', sa.JSON(), nullable=True))
    op.add_column('fields', sa.Column('can_improve_ai', sa.Boolean(), nullable=False))
    op.drop_column('fields', 'type')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('fields', sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('fields', 'can_improve_ai')
    op.drop_column('fields', 'filter_field')
    op.drop_column('fields', 'mask')
    # ### end Alembic commands ###
