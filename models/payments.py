from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base
from sqlalchemy import Enum, Integer, BigInteger, String, DateTime, ForeignKey, Float, func
from typing import Optional, TYPE_CHECKING
from datetime import datetime
from models.enums import PaymentMethodEnum, PaymentStatusEnum

if TYPE_CHECKING:
    from models.orders import Orders
    from models.user import User



class Payments(Base):

    """ To'lovlar jadvali modeli. Bu jadvalda buyurtmalar uchun to'lovlar haqida ma'lumotlar saqlanadi.  """

    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    order_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("orders.id"), nullable=False)
    payment_method: Mapped[PaymentMethodEnum] = mapped_column(Enum(PaymentMethodEnum), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[PaymentStatusEnum] = mapped_column(Enum(PaymentStatusEnum), default=PaymentStatusEnum.PENDING, nullable=False)

    # Chek (karta o'tkazma uchun)
    receipt_file_id: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    receipt_uploaded_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    # Admin tasdiqlash
    confirmed_by: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("users.id"), nullable=True)
    confirmed_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    rejection_reason: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relationships
    order: Mapped["Orders"] = relationship("Orders", back_populates="payment")
    confirmed_by_user: Mapped[Optional["User"]] = relationship("User", foreign_keys=[confirmed_by])

    def __repr__(self):
        return f"<To'lov: Buyurtma #{self.order_id}, {self.payment_method.value}, {self.amount}, {self.status.value}>"
