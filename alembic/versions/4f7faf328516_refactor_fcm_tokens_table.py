from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '4f7faf328516'
down_revision: Union[str, None] = '76bb67996247'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Drop and recreate fcm_tokens table with new schema."""
    # 1. Удаляем старую таблицу
    op.drop_table('fcm_tokens')

    # 2. Создаём заново с нужной структурой
    op.create_table(
        'fcm_tokens',
        sa.Column('id', sa.BigInteger(), primary_key=True, autoincrement=True),
        sa.Column('token', sa.String(length=255), nullable=False),
        sa.Column('user_id', sa.BigInteger(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('device_id', sa.String(length=255), nullable=False),
    )


def downgrade() -> None:
    """Rollback to old fcm_tokens table definition."""
    # 1. Удаляем новую таблицу
    op.drop_table('fcm_tokens')

    # 2. Восстанавливаем старую
    op.create_table(
        'fcm_tokens',
        sa.Column('token', sa.String(length=255), primary_key=True),
        sa.Column('user_id', sa.BigInteger(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('device_id', sa.String(length=255), nullable=False),
    )