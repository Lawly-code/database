from datetime import datetime

from sqlalchemy import BigInteger, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db_models.db_session import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    templates: Mapped[list["Template"]] = relationship("Template", back_populates="user")
    documents_creation: Mapped[list["DocumentCreation"]] = relationship("DocumentCreation", back_populates="user")
    messages: Mapped[list["Message"]] = relationship("Message", back_populates="user", lazy="selectin")
    subscribes: Mapped[list["Subscribe"]] = relationship("Subscribe", back_populates="user", lazy="selectin")
    payments: Mapped[list["Payment"]] = relationship("Payment", back_populates="user", lazy="selectin")
    lawyer: Mapped["Lawyer"] = relationship("Lawyer", back_populates="user", uselist=False, lazy="selectin")
