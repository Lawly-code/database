from sqlalchemy import BigInteger, String, ForeignKey, JSON
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from .db_session import Base


class Field(Base):
    __tablename__ = "fields"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    name_ru: Mapped[str] = mapped_column(String(255), nullable=False)
    example: Mapped[str] = mapped_column(String, nullable=True)
    mask: Mapped[str] = mapped_column(String(255), nullable=True)
    filter_field: Mapped[dict] = mapped_column(JSON, nullable=True)
    can_improve_ai: Mapped[bool] = mapped_column(default=False)
    document_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("documents.id"), nullable=True)
    template_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("templates.id"), nullable=True)

    template: Mapped["Template"] = relationship(
        "Template",
        back_populates="fields",
        lazy="selectin",
        passive_deletes=True
    )

    document: Mapped["Document"] = relationship(
        "Document",
        back_populates="fields",
        lazy="selectin",
        passive_deletes=True
    )
