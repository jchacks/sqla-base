"""empty message

Revision ID: 7b79f33ace8e
Revises: 
Create Date: 2018-10-22 14:24:16.842748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b79f33ace8e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('setting',
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('value', sa.String(length=1024), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('setting')
    # ### end Alembic commands ###
