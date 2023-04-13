"""add content column to posts table

Revision ID: 73baac9a00a7
Revises: db871999fcfa
Create Date: 2023-04-13 11:45:53.413002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73baac9a00a7'
down_revision = 'db871999fcfa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
