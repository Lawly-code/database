from sqlalchemy import String, ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from .db_session import Base


class Template(Base):
    __tablename__ = "templates"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    name_ru: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    image_url: Mapped[str] = mapped_column(String, nullable=False)
    download_url: Mapped[str] = mapped_column(String, nullable=False)


    documents: Mapped[list["DocumentCreation"]] = relationship("DocumentCreation", back_populates="template",
                                                               cascade="all, delete-orphan",
                                                               passive_deletes=True,
                                                               lazy="selectin")
    fields: Mapped[list["Field"]] = relationship("Field", back_populates="template", cascade="all, delete-orphan",
                                                 passive_deletes=True, lazy="selectin")
