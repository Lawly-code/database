from datetime import datetime

from sqlalchemy import BigInteger, DateTime, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .db_session import Base
from .enum_models import LawyerRequestStatusEnum
from sqlalchemy import Enum as SQLAlchemyEnum


class LawyerRequest(Base):
    __tablename__ = "lawyer_requests"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    lawyer_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("lawyers.id", ondelete="CASCADE"), nullable=True)
    status: Mapped[LawyerRequestStatusEnum] = mapped_column(SQLAlchemyEnum(LawyerRequestStatusEnum),
                                                            default=LawyerRequestStatusEnum.PENDING)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    document_url: Mapped[str] = mapped_column(String)
    note: Mapped[str] = mapped_column(String, default=None, nullable=True)
