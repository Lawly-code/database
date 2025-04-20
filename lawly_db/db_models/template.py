from sqlalchemy import String, ForeignKey, BigInteger
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from .db_session import Base


class Template(Base):
    __tablename__ = "templates"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    name_ru: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    image_url: Mapped[str] = mapped_column(String, nullable=False)

    documents: Mapped[list["DocumentCreation"]] = relationship("DocumentCreation", back_populates="template",
                                                               lazy="selectin")
    fields: Mapped[list["Field"]] = relationship("Field", back_populates="template", lazy="selectin")

    async def save(self, session: AsyncSession):
        session.add(self)
        await session.commit()
