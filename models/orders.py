from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base
from sqlalchemy import Enum, Integer, BigInteger, String, Boolean, DateTime, ForeignKey, Float, func
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime
from models.enums import DeliveryTypesEnum, OrderStatusEnum

if TYPE_CHECKING:
    from models.user import User
    from models.branches import Branches
    from models.user_address import UserAddresses
    from models.discounts import Discounts
    from models.order_items import OrderItems
    from models.payments import Payments



class Orders(Base):

    """ Buyurtmalar jadvali modeli. Bu jadvalda foydalanuvchilarning buyurtmalari haqida ma'lumotlar saqlanadi.  """

    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    order_number: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)

    # Yetkazib berish
    delivery_type: Mapped[DeliveryTypesEnum] = mapped_column(Enum(DeliveryTypesEnum), nullable=False)
    branch_id: Mapped[Optional[int]] = mapped_column(BigInteger, ForeignKey("branches.id"), nullable=True)
    address_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("user_addresses.id"), nullable=True)

    # Narxlar
    subtotal: Mapped[float] = mapped_column(Float, nullable=False)
    discount_id: Mapped[Optional[int]] = mapped_column(BigInteger, ForeignKey("discounts.id"), nullable=True)
    discount_percentage: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    discount_price: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    delivery_fee: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    total_price: Mapped[float] = mapped_column(Float, nullable=False)

    # Holat
    status: Mapped[OrderStatusEnum] = mapped_column(Enum(OrderStatusEnum), default=OrderStatusEnum.PENDING, nullable=False)
    is_paid: Mapped[bool] = mapped_column(Boolean, default=False)
    admin_note: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="orders")
    branch: Mapped[Optional["Branches"]] = relationship("Branches", back_populates="orders")
    address: Mapped[Optional["UserAddresses"]] = relationship("UserAddresses", back_populates="orders")
    discount: Mapped[Optional["Discounts"]] = relationship("Discounts", back_populates="orders")
    order_items: Mapped[List["OrderItems"]] = relationship("OrderItems", back_populates="order", cascade="all, delete-orphan")
    payment: Mapped[Optional["Payments"]] = relationship("Payments", back_populates="order", uselist=False)

    def __repr__(self):
        return f"<Buyurtma: #{self.order_number}, User: {self.user_id}, Jami: {self.total_price}>"
