from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base
from sqlalchemy import Integer, BigInteger, String, DateTime, ForeignKey, Float, func
from typing import Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from models.orders import Orders
    from models.print_prices import PrintPrices
    from models.binding_prices import BindingPrices




class OrderItems(Base):

    """ Buyurtma tarkibi jadvali modeli. Bu jadvalda buyurtmadagi har bir kitob haqida ma'lumotlar saqlanadi.  """

    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    order_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("orders.id"), nullable=False)
    file_id: Mapped[str] = mapped_column(String(255), nullable=False)
    file_name: Mapped[str] = mapped_column(String(255), nullable=False)
    page_count: Mapped[int] = mapped_column(Integer, nullable=False)
    copies: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    print_price_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("print_prices.id"), nullable=False)
    binding_price_id: Mapped[Optional[int]] = mapped_column(BigInteger, ForeignKey("binding_prices.id"), nullable=True)
    item_price: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relationships
    order: Mapped["Orders"] = relationship("Orders", back_populates="order_items")
    print_price: Mapped["PrintPrices"] = relationship("PrintPrices", back_populates="order_items")
    binding_price: Mapped[Optional["BindingPrices"]] = relationship("BindingPrices", back_populates="order_items")

    def __repr__(self):
        return f"<Buyurtma item: Order #{self.order_id}, Betlar: {self.page_count}, Nusxa: {self.copies}>"
