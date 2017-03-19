"""empty message

Revision ID: 7b1f9443da20
Revises: d8ced67afbb6
Create Date: 2017-03-19 04:16:24.385172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b1f9443da20'
down_revision = 'd8ced67afbb6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'employees', 'roles', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'employees', type_='foreignkey')
    # ### end Alembic commands ###
