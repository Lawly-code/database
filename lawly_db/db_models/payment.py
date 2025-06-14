from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Integer, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum as SQLAlchemyEnum

from .db_session import Base
from .enum_models import PaymentStatusEnum


class Payment(Base):
    __tablename__ = "payments"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[PaymentStatusEnum] = mapped_column(SQLAlchemyEnum(PaymentStatusEnum), nullable=False)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    subscribe_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("subscribes.id", ondelete="CASCADE"), nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="payments", lazy="selectin")
    subscribe: Mapped["Subscribe"] = relationship("Subscribe", back_populates="payments", lazy="selectin")
