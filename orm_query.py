from models import User
from sqlalchemy.orm import Session
from sqlalchemy import create_engine 
from connect import database_url


engine = create_engine(database_url, echo=True)

with Session(engine) as session:
    user = session.get(User,1)
    print("\nUser Details:")
    print(f"{user.username}  \n{user.email}")