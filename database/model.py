from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import (
    Column,
    BIGINT,
    Boolean,
    DateTime,
    Integer,
    SmallInteger,
    String,
    text,
    
)
from .base import Base, TableNameMixin


# Define your User classes
class User(Base, TableNameMixin):
    user_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=False)
    use_count: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    rating: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    bio: Mapped[str] = mapped_column(String(30), nullable=True)
    created_at: Mapped[datetime] = Column(DateTime, server_default=text("CURRENT_DATE"))

    def __repr__(self):
        return f"<User {self.user_id}>"


 