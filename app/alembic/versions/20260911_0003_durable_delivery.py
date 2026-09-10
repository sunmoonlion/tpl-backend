"""Template durable delivery, consumer fencing and recovery."""
from app.infrastructure.messaging.delivery_schema import downgrade, upgrade  # noqa: F401

revision = "20260911_0003"
down_revision = "20260801_0002"
branch_labels = None
depends_on = None
