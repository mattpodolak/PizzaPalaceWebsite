"""address table

Revision ID: 9247a039c8b3
Revises: b5550e0168d3
Create Date: 2018-07-17 17:47:37.710749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9247a039c8b3'
down_revision = 'b5550e0168d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=140), nullable=True),
    sa.Column('addressone', sa.String(length=140), nullable=True),
    sa.Column('addresstwo', sa.String(length=140), nullable=True),
    sa.Column('city', sa.String(length=140), nullable=True),
    sa.Column('postalcode', sa.String(length=140), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('ix_post_timestamp', table_name='post')
    op.drop_table('post')
    op.add_column('user', sa.Column('firstname', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('lastname', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('phone', sa.String(length=120), nullable=True))
    op.create_index(op.f('ix_user_phone'), 'user', ['phone'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_phone'), table_name='user')
    op.drop_column('user', 'phone')
    op.drop_column('user', 'lastname')
    op.drop_column('user', 'firstname')
    op.create_table('post',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('body', sa.VARCHAR(length=140), nullable=True),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_post_timestamp', 'post', ['timestamp'], unique=False)
    op.drop_table('address')
    # ### end Alembic commands ###