"""guaranties added

Revision ID: 7199926a2e4b
Revises: 93be6b16c448
Create Date: 2021-01-12 01:06:33.319197

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7199926a2e4b'
down_revision = '93be6b16c448'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('GuarantiesPage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('AdmissionStage')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('AdmissionStage',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('stage_img', sa.VARCHAR(length=100), nullable=False),
    sa.Column('title', sa.TEXT(), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('GuarantiesPage')
    # ### end Alembic commands ###
