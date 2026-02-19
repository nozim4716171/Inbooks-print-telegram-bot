from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base
from sqlalchemy import Enum, Integer, BigInteger, String, DateTime, ForeignKey, Float, func
from typing import Optional, TYPE_CHECKING
from datetime import datetime
from models.enums import BookFormatsEnum, PrintTypesEnum, BindingTypesEnum

if TYPE_CHECKING:
    from models.user import User



class CartItems(Base):

    """ Savatcha jadvali modeli. Bu jadvalda foydalanuvchilarning savatchasidagi kitoblar haqida ma'lumotlar saqlanadi.  """

    __tablename__ = "cart_items"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    file_id: Mapped[str] = mapped_column(String(255), nullable=False)
    file_name: Mapped[str] = mapped_column(String(255), nullable=False)
    page_count: Mapped[int] = mapped_column(Integer, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    book_format: Mapped[BookFormatsEnum] = mapped_column(Enum(BookFormatsEnum), nullable=False)
    print_type: Mapped[PrintTypesEnum] = mapped_column(Enum(PrintTypesEnum), nullable=False)
    binding_type: Mapped[Optional[BindingTypesEnum]] = mapped_column(Enum(BindingTypesEnum), nullable=True)
    item_price: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="cart_items")

    def __repr__(self):
        return f"<Savatcha: {self.file_name}, {self.book_format.value}, {self.print_type.value}, {self.quantity} nusxa>"
