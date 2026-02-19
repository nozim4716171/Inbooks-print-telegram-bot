from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base
from sqlalchemy import Float, Integer, DateTime, Boolean, BigInteger, func
from typing import List, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from models.orders import Orders


class Discounts(Base):

    """ Chegirmalar jadvali modeli. Bu jadvalda botdagi chegirmalar haqida ma'lumotlar saqlanadi.  """

    __tablename__ = "discounts"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    min_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    discount_percentage: Mapped[float] = mapped_column(Float, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    orders: Mapped[List["Orders"]] = relationship("Orders", back_populates="discount")

    def __repr__(self):
        return f"<Chegirma: {self.discount_percentage}%, Minimal miqdor: {self.min_quantity}>"
