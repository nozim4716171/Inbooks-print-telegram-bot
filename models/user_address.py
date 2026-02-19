from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base
from sqlalchemy import Integer, String, DateTime, ForeignKey, Float, func
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from models.user import User
    from models.orders import Orders



class UserAddresses(Base):

    """ Foydalanuvchilarning manzillari jadvali modeli. Bu jadvalda foydalanuvchilarning manzillari haqida ma'lumotlar saqlanadi.  """

    __tablename__ = "user_addresses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    address: Mapped[str] = mapped_column(String(255), nullable=False)
    latitude: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    longitude: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    user: Mapped["User"] = relationship("User", back_populates="user_addresses")
    orders: Mapped[List["Orders"]] = relationship("Orders", back_populates="address")

    def __repr__(self):
        return f"<Manzil: {self.title}, Foydalanuvchi ID: {self.user_id}>"
