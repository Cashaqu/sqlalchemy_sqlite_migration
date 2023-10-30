"""Creation

Revision ID: 523ed2c32923
Revises: a3651f21f5ea
Create Date: 2023-10-31 01:08:15.714819

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '523ed2c32923'
down_revision: Union[str, None] = 'a3651f21f5ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('publisher',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shop',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.Integer(), nullable=False),
        sa.Column('id_publisher', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['id_publisher'], ['publisher.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stock',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('id_book', sa.Integer(), nullable=False),
        sa.Column('id_shop', sa.Integer(), nullable=False),
        sa.Column('count', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['id_book'], ['book.id'], ),
        sa.ForeignKeyConstraint(['id_shop'], ['shop.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sale',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('price', sa.Float(), nullable=False),
        sa.Column('date_sale', sa.DateTime(), nullable=False),
        sa.Column('id_stock', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['id_stock'], ['stock.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sale')
    op.drop_table('stock')
    op.drop_table('book')
    op.drop_table('shop')
    op.drop_table('publisher')
    # ### end Alembic commands ###