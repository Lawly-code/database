from datetime import datetime

from sqlalchemy import BigInteger, ForeignKey, DateTime, String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from db_models.db_session import Base
from sqlalchemy import Enum as SQLAlchemyEnum
from models.enum_models import DocumentStatusEnum


class DocumentCreation(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    template_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("templates.id", ondelete="CASCADE"), nullable=True,
                                             default=None)
    status: Mapped[DocumentStatusEnum] = mapped_column(SQLAlchemyEnum(DocumentStatusEnum), nullable=False)
    start_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    end_date: Mapped[datetime] = mapped_column(DateTime, default=None, nullable=True)
    custom_name: Mapped[str] = mapped_column(String, nullable=True, default=None)
    error_message: Mapped[str] = mapped_column(String, nullable=True, default=None)

    template: Mapped["Template"] = relationship("Template", back_populates="documents", lazy="selectin")
    user: Mapped["User"] = relationship("User", back_populates="documents_creation", lazy="selectin")
