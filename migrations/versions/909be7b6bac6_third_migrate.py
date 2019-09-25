"""third migrate

Revision ID: 909be7b6bac6
Revises: 6b3c58221868
Create Date: 2019-09-25 11:04:08.286969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '909be7b6bac6'
down_revision = '6b3c58221868'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('category', sa.Integer(), nullable=True))
    op.drop_constraint('pitches_category_id_fkey', 'pitches', type_='foreignkey')
    op.create_foreign_key(None, 'pitches', 'categories', ['category'], ['id'])
    op.drop_column('pitches', 'category_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.create_foreign_key('pitches_category_id_fkey', 'pitches', 'categories', ['category_id'], ['id'])
    op.drop_column('pitches', 'category')
    # ### end Alembic commands ###
