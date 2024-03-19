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
    balance: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    invited_count: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    joined: Mapped[bool] = Column(Boolean, default=False)
    viewed: Mapped[bool] = Column(Boolean, default=False)

    
    

    def __repr__(self):
        return f"<User {self.user_id}>"

