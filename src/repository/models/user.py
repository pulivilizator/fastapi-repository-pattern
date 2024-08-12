from uuid import UUID

from sqlalchemy import Uuid, text, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import TimeStampMixin


class User(Base, TimeStampMixin):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, server_default=text('gen_random_uuid()'))
    username: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(128), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    is_manager: Mapped[bool] = mapped_column(Boolean, default=False)
    is_customer: Mapped[bool] = mapped_column(Boolean, default=True)
