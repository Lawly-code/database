from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from db_models.db_session import Base


class Document(Base):
    __tablename__ = "documents"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    name_ru: Mapped[str] = mapped_column(String(255), nullable=False)
    link: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)

    fields: Mapped[list["DocumentField"]] = mapped_column("fields", back_populates="document", lazy="selectin")
