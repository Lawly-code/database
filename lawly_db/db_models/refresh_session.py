import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import BigInteger, ForeignKey, String, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column

from .db_session import Base


class RefreshSession(Base):
    __tablename__ = "refresh_sessions"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)
    refresh_token: Mapped[uuid.UUID]
    device_os: Mapped[str] = mapped_column(String)
    device_name: Mapped[str] = mapped_column(String)
    device_id: Mapped[str] = mapped_column(String)
    ip: Mapped[Optional[str]] = mapped_column(String(15))
    expires_in: Mapped[int] = mapped_column(BigInteger)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
