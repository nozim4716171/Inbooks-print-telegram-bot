from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base
from sqlalchemy import Integer, BigInteger, String, Boolean, DateTime, func
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from models.user_address import UserAddresses
    from models.feedbacks import Feedbacks
    from models.orders import Orders
    from models.cart_items import CartItems




class User(Base):

    """ Foydalanuvchilar jadvali modeli. Bu jadvalda bot foydalanuvchilari haqida ma'lumotlar saqlanadi.  """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    phone_number: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    language: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_blocked: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    user_addresses: Mapped[List["UserAddresses"]] = relationship("UserAddresses", back_populates="user", cascade="all, delete-orphan")
    feedbacks: Mapped[List["Feedbacks"]] = relationship("Feedbacks", back_populates="user", cascade="all, delete-orphan")
    orders: Mapped[List["Orders"]] = relationship("Orders", back_populates="user", cascade="all, delete-orphan")
    cart_items: Mapped[List["CartItems"]] = relationship("CartItems", back_populates="user", cascade="all, delete-orphan")


    def __repr__(self):
        return f"<Ism: {self.first_name} {self.last_name}, Telegram ID: {self.telegram_id}>"
