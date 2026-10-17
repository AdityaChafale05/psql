import os
from sqlalchemy import create_engine , text
from sqlalchemy.engine import URL


database_url = URL.create(
    drivername = 'postgresql+psycopg',
    host = 'localhost',
    port =5432,
    database ='devblog',
    username = 'devblog_user',
    password = os.environ["DB_PASSWORD"]
) 

engine = create_engine(database_url, echo=True)

query = text("select * from users")

with engine.connect() as conn:
    result = conn.execute(query)

for row in result:
    print(row)
