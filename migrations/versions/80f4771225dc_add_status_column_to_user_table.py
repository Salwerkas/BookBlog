"""add status column to user table

Revision ID: 80f4771225dc
Revises: 3355714a8063
Create Date: 2019-03-07 21:23:45.016035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80f4771225dc'
down_revision = '3355714a8063'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('status', sa.CHAR(length=1), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'status')
    # ### end Alembic commands ###
