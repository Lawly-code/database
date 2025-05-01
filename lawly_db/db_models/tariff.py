from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .db_session import Base


class Tariff(Base):
    __tablename__ = "tariffs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    consultations_count: Mapped[int] = mapped_column(Integer, default=0)
    ai_access: Mapped[bool] = mapped_column(default=False)
    custom_templates: Mapped[bool] = mapped_column(default=False)
    unlimited_docs: Mapped[bool] = mapped_column(default=False)
