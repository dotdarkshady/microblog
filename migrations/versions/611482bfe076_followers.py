"""followers

Revision ID: 611482bfe076
Revises: cf5fa2be2e8b
Create Date: 2018-07-01 15:44:02.557430

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '611482bfe076'
down_revision = 'cf5fa2be2e8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
                    sa.Column('follower_id', sa.Integer(), nullable=True),
                    sa.Column('followed_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
                    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
