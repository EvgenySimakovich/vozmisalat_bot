from sqlalchemy import String, func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(String(30))
    is_created: Mapped[datetime] = mapped_column(insert_default=datetime.now())
    promo: Mapped[str] = mapped_column(String(20), nullable=True)

    def __repr__(self) -> str:
        return f'User (id={self.id!r}, name={self.username!r})'
