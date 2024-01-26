"""coincap

Revision ID: 1feb5e386d24
Revises: fe98523b5bb7
Create Date: 2024-01-27 16:33:44.978866

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1feb5e386d24'
down_revision: Union[str, None] = 'fe98523b5bb7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tracker', sa.Column('usd_price', sa.String(), nullable=True))
    op.drop_column('tracker', 'usdPrice')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tracker', sa.Column('usdPrice', sa.VARCHAR(), nullable=True))
    op.drop_column('tracker', 'usd_price')
    # ### end Alembic commands ###
