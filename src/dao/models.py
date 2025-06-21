import os

from sqlalchemy import Column, Integer, String, Boolean, DateTime, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, UTC

from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'servbot_users'

    telegram_id = Column(Integer, primary_key=True)  # ID пользователя в Telegram
    username = Column(String(50), nullable=True)  # @username (может быть None, если скрыт)
    first_name = Column(String(50), nullable=False)  # Имя
    last_name = Column(String(50), nullable=True)  # Фамилия (может быть None)
    phone = Column(String(20), nullable=True)  # Телефон (если пользователь его предоставит)
    is_admin = Column(Boolean, default=False)  # Админ ли?
    is_active = Column(Boolean, default=True)  # Активен ли аккаунт?
    registered_at = Column(DateTime, default=datetime.now(tz=UTC))  # Дата регистрации

    def __repr__(self):
        return f"<User(id={self.telegram_id}, username='{self.username}')>"


engine = create_engine(
    os.getenv("SERVBOT_DATABASE_URL", "sqlite:///servbot.db"),
    echo=True
)

AsyncSessionLocal = None
if SERVBOT_ASYNC_DATABASE_URL := os.getenv("SERVBOT_ASYNC_DATABASE_URL"):
    async_engine = create_async_engine(
        os.getenv("SERVBOT_ASYNC_DATABASE_URL", "sqlite+aiosqlite:///servbot.db"),
        echo=True
    )

    AsyncSessionLocal = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False) # NoQa
