"""empty message

Revision ID: e187b65f7f1b
Revises: 58fc2c4c30a5
Create Date: 2021-04-01 21:03:04.872235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e187b65f7f1b'
down_revision = '58fc2c4c30a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin_user', sa.Column('remark', sa.String(length=255), nullable=True, comment='备注'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('admin_user', 'remark')
    # ### end Alembic commands ###
