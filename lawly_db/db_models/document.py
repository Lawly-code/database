from sqlalchemy import BigInteger, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .db_session import Base


class Document(Base):
    __tablename__ = "documents"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_personal: Mapped[bool] = mapped_column(Boolean, server_default='false')
    name_ru: Mapped[str] = mapped_column(String(255), nullable=False)
    link: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)

    fields: Mapped[list["Field"]] = relationship("Field", back_populates="document", lazy="selectin")
