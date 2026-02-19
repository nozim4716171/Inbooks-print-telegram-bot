from database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, Boolean, BigInteger, Enum, Float, String, func
from typing import List, TYPE_CHECKING
from datetime import datetime
from models.enums import BindingTypesEnum

if TYPE_CHECKING:
    from models.order_items import OrderItems



class BindingPrices(Base):

    """ Bosma narxlari jadvali modeli. Bu jadvalda bosma xizmatining narxlari haqida ma'lumotlar saqlanadi.  """

    __tablename__ = "binding_prices"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    binding_type: Mapped[BindingTypesEnum] = mapped_column(Enum(BindingTypesEnum), nullable=False)
    format: Mapped[str] = mapped_column(String(255), nullable=False)
    price_per_book: Mapped[float] = mapped_column(Float, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    order_items: Mapped[List["OrderItems"]] = relationship("OrderItems", back_populates="binding_price")

    def __repr__(self):
        return f"<Bosma narxi: {self.binding_type.value}, Format: {self.format}, Narx: {self.price_per_book}>"
