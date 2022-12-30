"""multi tables

Revision ID: 5cc2e04d2e38
Revises: 
Create Date: 2022-12-29 14:21:57.104817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5cc2e04d2e38'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('recipe_id', sa.Integer(), nullable=True),
    sa.Column('measurement_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['measurement_id'], ['measurement.id'], ),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipe.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('ingredient', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_ingredient_name'), ['name'], unique=False)

    op.create_table('measurement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('ingredient_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('measurement', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_measurement_name'), ['name'], unique=False)

    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('recipe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_recipe_title'), ['title'], unique=False)

    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_recipe_title'))

    op.drop_table('recipe')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    with op.batch_alter_table('measurement', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_measurement_name'))

    op.drop_table('measurement')
    with op.batch_alter_table('ingredient', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_ingredient_name'))

    op.drop_table('ingredient')
    # ### end Alembic commands ###

