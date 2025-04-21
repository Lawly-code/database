from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column
from sqlalchemy import Enum as SQLAlchemyEnum

from .db_session import Base
from .enum_models import FieldTypeENum


class Field(Base):
    __tablename__ = "fields"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    type: Mapped[FieldTypeENum] = mapped_column(SQLAlchemyEnum(FieldTypeENum), nullable=False)
    document_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("documents.id"), nullable=False)
    template_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("templates.id"), nullable=False)

    template: Mapped["Template"] = relationship("Template", back_populates="fields", lazy="selectin")
    document: Mapped["Document"] = relationship("Document", back_populates="fields", lazy="selectin")
