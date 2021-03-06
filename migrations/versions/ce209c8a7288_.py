"""empty message

Revision ID: ce209c8a7288
Revises: 37d8172b7569
Create Date: 2017-03-17 03:40:12.701681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce209c8a7288'
down_revision = '37d8172b7569'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employees', sa.Column('email', sa.String(length=60), nullable=True))
    op.add_column('employees', sa.Column('is_admin', sa.Boolean(), nullable=True))
    op.create_index(op.f('ix_employees_email'), 'employees', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_employees_email'), table_name='employees')
    op.drop_column('employees', 'is_admin')
    op.drop_column('employees', 'email')
    # ### end Alembic commands ###
