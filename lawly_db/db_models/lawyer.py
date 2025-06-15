from datetime import datetime

from sqlalchemy import BigInteger, ForeignKey, DateTime, TIMESTAMP, func
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from .db_session import Base


class Lawyer(Base):
    __tablename__ = "lawyers"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())

    user: Mapped["User"] = relationship("User", back_populates="lawyer", lazy="selectin")
