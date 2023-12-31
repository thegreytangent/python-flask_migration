"""empty message

Revision ID: 586bc89f3d88
Revises: 3466de3d121a
Create Date: 2023-07-30 23:18:53.985959

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '586bc89f3d88'
down_revision = '3466de3d121a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('content',
               existing_type=mysql.TEXT(),
               type_=sa.String(length=255),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('content',
               existing_type=sa.String(length=255),
               type_=mysql.TEXT(),
               existing_nullable=True)

    # ### end Alembic commands ###
