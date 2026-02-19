from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base
from sqlalchemy import Integer, DateTime, Boolean, BigInteger,ForeignKey, Text, func
from typing import Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from models.user import User




class Feedbacks(Base):
    
    """ Fikr-mulohazalar jadvali modeli. Bu jadvalda foydalanuvchilarning fikr-mulohazalari haqida ma'lumotlar saqlanadi.  """

    __tablename__ = "feedbacks"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    is_read: Mapped[bool] = mapped_column(Boolean, default=False)
    admin_reply: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    user: Mapped["User"] = relationship("User", back_populates="feedbacks")

    def __repr__(self):
        return f"<Fikr-mulohaza: {self.message[:20]}..., Foydalanuvchi ID: {self.user_id}>"