from datetime import datetime

from sqlalchemy import BigInteger, ForeignKey, String, DateTime
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Enum as SQLAlchemyEnum

from .db_session import Base
from .enum_models import DocumentReviewStatusEnum


class DocumentReview(Base):
    __tablename__ = "document_reviews"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    lawyer_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("lawyers.id", ondelete="CASCADE"), nullable=False)
    document_content: Mapped[str] = mapped_column(String, nullable=False)
    document_url: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[DocumentReviewStatusEnum] = mapped_column(SQLAlchemyEnum(DocumentReviewStatusEnum),
                                                             default=DocumentReviewStatusEnum.PENDING)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    feedback: Mapped[str] = mapped_column(String, default=None, nullable=True)
    corrected_document_url: Mapped[str] = mapped_column(String, default=None, nullable=True)
