import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped ,mapped_column
from sqlalchemy import Identity, Integer,String,DateTime, text 


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ ="users"
    
    
    id : Mapped[int] = mapped_column(
        Integer,
        Identity(always=True),
        primary_key =True,
        )
    
    username :Mapped[str] = mapped_column(
        String(20),
        nullable = False,
        unique =True,
        )
    
    email : Mapped[str] =mapped_column(
        String(20),
        nullable =False,
        unique=True,
        )
    
    created_at : Mapped[datetime]  = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("Current_timestamp"),
        )
    