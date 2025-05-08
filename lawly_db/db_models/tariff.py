from sqlalchemy import Integer, String, ARRAY, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .db_session import Base


class Tariff(Base):
    __tablename__ = "tariffs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    is_base: Mapped[bool] = mapped_column(default=False)
    features: Mapped[list[str]] = mapped_column(ARRAY(VARCHAR), default=[])
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    consultations_count: Mapped[int] = mapped_column(Integer, default=0)
    ai_access: Mapped[bool] = mapped_column(default=False)
    custom_templates: Mapped[bool] = mapped_column(default=False)
    unlimited_docs: Mapped[bool] = mapped_column(default=False)

    subscribes: Mapped[list["Subscribe"]] = relationship(
        "Subscribe",
        back_populates="tariff",
        cascade="all, delete-orphan",
        passive_deletes=True,
        single_parent=True,
        lazy="selectin"
    )

