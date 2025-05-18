"""refactor lawyer request enum status

Revision ID: 988801dbac3f
Revises: bdd4f3c73892
Create Date: 2025-05-18 20:00:06.212306

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '988801dbac3f'
down_revision: Union[str, None] = 'bdd4f3c73892'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("ALTER TYPE lawyerrequeststatusenum ADD VALUE IF NOT EXISTS 'COMPLETED';")
    op.execute("ALTER TYPE lawyerrequeststatusenum ADD VALUE IF NOT EXISTS 'PENDING';")
    op.execute("ALTER TYPE lawyerrequeststatusenum ADD VALUE IF NOT EXISTS 'PROCESSING';")
    op.execute("ALTER TYPE chattypeenum ADD VALUE IF NOT EXISTS 'LAWYER';")
    op.execute("ALTER TYPE chattypeenum ADD VALUE IF NOT EXISTS 'AI';")
    op.execute("ALTER TYPE messagesendertypeenum ADD VALUE IF NOT EXISTS 'USER';")
    op.execute("ALTER TYPE messagesendertypeenum ADD VALUE IF NOT EXISTS 'AI';")
    op.execute("ALTER TYPE messagesendertypeenum ADD VALUE IF NOT EXISTS 'LAWYER';")


def downgrade() -> None:
    """Downgrade schema."""
    # PostgreSQL НЕ поддерживает удаление значений из ENUM напрямую.
    # Для отката нужно пересоздавать ENUM вручную, поэтому оставляем пустым.
    pass