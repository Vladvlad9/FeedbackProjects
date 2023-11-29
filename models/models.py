from datetime import datetime
from typing import Annotated

from sqlalchemy import Boolean, BigInteger, String, DateTime, Integer, Column
from sqlalchemy.orm import declarative_base

# from sqlalchemy.orm import declarative_base, mapped_column, Mapped


Base = declarative_base()
#
# intPK = Annotated[int, mapped_column(primary_key=True)]


# class User(Base):
#     __tablename__: str = 'users'
#
#     id: Mapped[intPK]
#     user_id = Column(BigInteger, nullable=False, unique=True, index=True, comment="User ID")
#     phone: Mapped[str] = mapped_column(nullable=False, unique=True, index=True, comment="Phone number")
#     is_active: Mapped[bool] = mapped_column(default=True, comment="Is the user active?")
#     created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, comment="Creation timestamp")
#     updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow,
#                                                  comment="Last update timestamp")

class User(Base):
    __tablename__: str = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, nullable=False, unique=True, index=True, comment="User ID")
    phone = Column(String, nullable=False, unique=True, index=True, comment="User ID")

    # phone: Mapped[str] = mapped_column(nullable=False, unique=True, index=True, comment="Phone number")
    # is_active: Mapped[bool] = mapped_column(default=True, comment="Is the user active?")
    # created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, comment="Creation timestamp")
    # updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow,
    #                                              comment="Last update timestamp")
