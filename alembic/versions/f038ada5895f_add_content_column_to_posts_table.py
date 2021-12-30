"""add content column to posts table

Revision ID: f038ada5895f
Revises: da8ea2999e88
Create Date: 2021-12-29 07:35:40.723515

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f038ada5895f'
down_revision = 'da8ea2999e88'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
