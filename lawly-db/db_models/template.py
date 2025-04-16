from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from db_models.db_session import Base


class Template(Base):
    __tablename__ = "templates"
    id: Mapped[int] = mapped_column()
    name: Mapped[str] = mapped_column(String(255), ForeignKey("users.name"), nullable=False)
    name_ru: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    image_url: Mapped[str] = mapped_column(String, nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="templates", lazy="selectin")
    documents: Mapped[list["DocumentCreation"]] = relationship("DocumentCreation", back_populates="template",
                                                               lazy="selectin")
    fields: Mapped[list["Field"]] = relationship("Field", back_populates="template", lazy="selectin")
