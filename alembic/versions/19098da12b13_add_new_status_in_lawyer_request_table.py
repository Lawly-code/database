"""add new status in lawyer_request table

Revision ID: 19098da12b13
Revises: 4f7faf328516
Create Date: 2025-05-17 19:10:05.972091
"""
from typing import Sequence, Union
from alembic import op


# revision identifiers, used by Alembic.
revision: str = '19098da12b13'
down_revision: Union[str, None] = '4f7faf328516'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Добавим новое значение в enum
    op.execute("ALTER TYPE lawyerrequeststatusenum ADD VALUE IF NOT EXISTS 'processing'")


def downgrade() -> None:
    """Downgrade schema."""
    # Откат Enum значения невозможен напрямую — PostgreSQL не поддерживает удаление значений из ENUM.
    # Для полноценного отката нужно пересоздать тип без 'processing', но это опасно в проде.
    pass