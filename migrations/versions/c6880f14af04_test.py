"""test

Revision ID: c6880f14af04
Revises: f79643ac25f8
Create Date: 2018-04-11 14:33:40.767205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6880f14af04'
down_revision = 'f79643ac25f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('review', sa.Column('test', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('review', 'test')
    # ### end Alembic commands ###