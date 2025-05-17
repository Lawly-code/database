import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import BigInteger, ForeignKey, String, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column

from .db_session import Base


class RefreshSessionLawyer(Base):
    __tablename__ = "refresh_sessions_lawyer"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    refresh_token: Mapped[uuid.UUID]
    user_agent: Mapped[str] = mapped_column(String(200))
    fingerprint: Mapped[str] = mapped_column(String(200))
    ip: Mapped[Optional[str]] = mapped_column(String(15))
    expires_in: Mapped[int] = mapped_column(BigInteger)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
