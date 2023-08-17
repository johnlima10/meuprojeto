"""db_criar_cadastro

Revision ID: c3c9ea3a2b8f
Revises: 89819dc865f6
Create Date: 2023-08-17 08:45:17.681063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3c9ea3a2b8f'
down_revision = '89819dc865f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cadastro_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=40), nullable=False),
    sa.Column('sobrenome', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('telefone', sa.String(length=14), nullable=False),
    sa.Column('senha', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cadastro_model')
    # ### end Alembic commands ###
