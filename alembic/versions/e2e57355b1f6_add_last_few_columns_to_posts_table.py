"""add last few columns to posts table

Revision ID: e2e57355b1f6
Revises: e8f3ee57c408
Create Date: 2023-04-13 15:18:08.896790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2e57355b1f6'
down_revision = 'e8f3ee57c408'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, 
                                     server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
                                     server_default=sa.text('now()'), nullable=False))

    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
