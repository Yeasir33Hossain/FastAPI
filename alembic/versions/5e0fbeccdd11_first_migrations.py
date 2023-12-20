"""first migrations

Revision ID: 5e0fbeccdd11
Revises: 2e6c3a1ce613
Create Date: 2023-12-20 16:08:43.761553

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e0fbeccdd11'
down_revision: Union[str, None] = '2e6c3a1ce613'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
