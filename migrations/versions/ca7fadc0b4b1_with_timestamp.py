"""with timestamp

Revision ID: ca7fadc0b4b1
Revises: 5cc2e04d2e38
Create Date: 2022-12-29 14:45:28.601742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca7fadc0b4b1'
down_revision = '5cc2e04d2e38'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timestamp', sa.DateTime(), nullable=True))
        batch_op.create_index(batch_op.f('ix_recipe_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_recipe_timestamp'))
        batch_op.drop_column('timestamp')

    # ### end Alembic commands ###

