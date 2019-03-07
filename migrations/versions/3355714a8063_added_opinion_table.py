"""added opinion table

Revision ID: 3355714a8063
Revises: 7a7caf255ee9
Create Date: 2019-02-28 20:30:00.569378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3355714a8063'
down_revision = '7a7caf255ee9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('opinion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_opinion_timestamp'), 'opinion', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_opinion_timestamp'), table_name='opinion')
    op.drop_table('opinion')
    # ### end Alembic commands ###