from datetime import datetime

from sqlalchemy import BigInteger, ForeignKey, String, DateTime, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum as SQLAlchemyEnum

from .db_session import Base
from .enum_models import ChatTypeEnum, MessageSenderTypeEnum, MessageStatusEnum


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    chat_type: Mapped[ChatTypeEnum] = mapped_column(SQLAlchemyEnum(ChatTypeEnum), nullable=False)
    sender_type: Mapped[MessageSenderTypeEnum] = mapped_column(SQLAlchemyEnum(MessageSenderTypeEnum), nullable=False)
    sender_id: Mapped[int] = mapped_column(BigInteger, nullable=True, default=None)
    text: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
    status: Mapped[MessageStatusEnum] = mapped_column(SQLAlchemyEnum(MessageStatusEnum), default=MessageStatusEnum.SENT)
    read_at: Mapped[datetime] = mapped_column(DateTime, default=None, nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="messages", lazy="selectin")
