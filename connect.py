import os
from sqlalchemy import create_engine , text
from sqlalchemy.engine import URL

# First step to connect to Database
database_url = URL.create(
    drivername = 'postgresql+psycopg',
    host = 'localhost',
    port =5432,
    database ='devblog',
    username = 'devblog_user',
    password = os.environ["DB_PASSWORD"]
) 

#Creating a Engine instance to connect to the database
engine = create_engine(database_url, echo=True)


query = text("select * from users")


#Power on the Engine and connect to the database
with engine.connect() as conn:
    result = conn.execute(query)

for row in result:
    print(row)
