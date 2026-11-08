"""add go_outside.

Revision ID: 4455d8219224
Revises: f6af308c367f
Create Date: 2026-11-08 19:21:53.413932

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4455d8219224'
down_revision: Union[str, Sequence[str], None] = 'f6af308c367f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('weather_wind', sa.Column('go_outside', sa.Boolean(), nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table('weather_wind') as batch_op:
        batch_op.drop_column('go_outside')
