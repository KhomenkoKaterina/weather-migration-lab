"""extract wind

Revision ID: f6af308c367f
Revises: 5c2f639295e5
Create Date: 2026-11-08 17:54:23.803351

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6af308c367f'
down_revision: Union[str, Sequence[str], None] = '5c2f639295e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('weather_wind',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('record_id', sa.Integer(), sa.ForeignKey('weather_record.id'), nullable=False),
        sa.Column('wind_kph', sa.Float(), nullable=False),
        sa.Column('wind_degree', sa.Integer(), nullable=False),
        sa.Column('wind_direction', sa.Enum(
            'N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW',
            name='winddirection'), nullable=False),
    )
    op.execute('INSERT INTO weather_wind (record_id, wind_kph, wind_degree, wind_direction) SELECT id, wind_kph, wind_degree, wind_direction FROM weather_record')
    with op.batch_alter_table('weather_record') as batch_op:
        batch_op.drop_column('wind_kph')
        batch_op.drop_column('wind_degree')
        batch_op.drop_column('wind_direction')



def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table('weather_record') as batch_op:
        batch_op.add_column(sa.Column('wind_kph', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('wind_degree', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('wind_direction', sa.Enum(
            'N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW',
            name='winddirection'), nullable=True))

    op.create_index('ix_weather_wind_record_id', 'weather_wind', ['record_id'])

    op.execute('UPDATE weather_record SET wind_kph = (SELECT wind_kph FROM weather_wind WHERE weather_wind.record_id = weather_record.id), wind_degree = (SELECT wind_degree FROM weather_wind WHERE weather_wind.record_id = weather_record.id), wind_direction = (SELECT wind_direction FROM weather_wind WHERE weather_wind.record_id = weather_record.id)')

    with op.batch_alter_table('weather_record') as batch_op:
        batch_op.alter_column('wind_kph', existing_type=sa.Float(), nullable=False)
        batch_op.alter_column('wind_degree', existing_type=sa.Integer(), nullable=False)
        batch_op.alter_column('wind_direction', existing_type=sa.Enum(
            'N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW',
            name='winddirection'), nullable=False)

    op.drop_index('ix_weather_wind_record_id', table_name='weather_wind')
    op.drop_table('weather_wind')