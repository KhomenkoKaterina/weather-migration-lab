"""initial

Revision ID: 5c2f639295e5
Revises: 
Create Date: 2026-11-08 12:12:34.920463

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5c2f639295e5'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'weather_record',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('country', sa.String(length=100), nullable=False),
        sa.Column('last_updated', sa.DateTime(), nullable=False),
        sa.Column('sunrise', sa.Time(), nullable=False),
        sa.Column('wind_kph', sa.Float(), nullable=False),
        sa.Column('wind_degree', sa.Integer(), nullable=False),
        sa.Column('wind_direction', sa.Enum(
            'N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW',
            name='winddirection'), nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('weather_record')
    
