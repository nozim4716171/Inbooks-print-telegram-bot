from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base
from sqlalchemy import DateTime, Boolean, BigInteger, Enum, Float, func
from typing import List, TYPE_CHECKING
from datetime import datetime
from models.enums import BookFormatsEnum, PrintTypesEnum

if TYPE_CHECKING:
    from models.order_items import OrderItems



class PrintPrices(Base):

    """ Chop etish narxlari jadvali modeli. Bu jadvalda chop etish narxlari haqida ma'lumotlar saqlanadi.  """

    __tablename__ = "print_prices"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    format: Mapped[BookFormatsEnum] = mapped_column(Enum(BookFormatsEnum), nullable=False)
    print_type: Mapped[PrintTypesEnum] = mapped_column(Enum(PrintTypesEnum), nullable=False)
    price_per_page: Mapped[float] = mapped_column(Float, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    order_items: Mapped[List["OrderItems"]] = relationship("OrderItems", back_populates="print_price")

    def __repr__(self):
        return f"<Chop etish narxi: Format: {self.format.value}, Chop turi: {self.print_type.value}, Narx: {self.price_per_page}>"
