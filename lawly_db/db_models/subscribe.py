from datetime import datetime

from sqlalchemy import BigInteger, ForeignKey, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .db_session import Base


class Subscribe(Base):
    __tablename__ = "subscribes"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    tariff_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("tariffs.id", ondelete="CASCADE"), nullable=False)
    start_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    count_lawyers: Mapped[int] = mapped_column(Integer, default=0)
    consultations_total: Mapped[int] = mapped_column(Integer, default=0)
    consultations_used: Mapped[int] = mapped_column(Integer, default=0)
    can_user_ai: Mapped[bool] = mapped_column(default=False)
    can_create_custom_templates: Mapped[bool] = mapped_column(default=False)
    unlimited_documents: Mapped[bool] = mapped_column(default=False)

    user: Mapped["User"] = relationship("User", back_populates="subscribe", lazy="selectin")
    payments: Mapped[list["Payment"]] = relationship("Payment", back_populates="subscribe", cascade="all, delete-orphan",
                                                         passive_deletes=True, lazy="selectin")
    tariff: Mapped["Tariff"] = relationship("Tariff", back_populates="subscribes", lazy="selectin")
