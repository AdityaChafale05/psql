from sqlalchemy.orm import DeclarativeBase, Mapped ,mapped_column
from sqlalchemy import Integer,String,DateTime 


class Base(DeclarativeBase):
    User