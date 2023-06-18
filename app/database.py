from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time

from .config import settings

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost/fastAPi"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
print(SQLALCHEMY_DATABASE_URL)
engine=create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()

def get_db():
    db=SessionLocal()
    try :
        yield db
    finally:
        db.close()


#connect to database through pyscopg2 to run raw sql queries. We changed i=to sqlAlchemy 
# while True:
#         try:
#             conn=psycopg2.connect(host='localhost',database='fastAPi',
#                                  user='postgres',password='admin',
#                                  cursor_factory=RealDictCursor)
#             cursor=conn.cursor()
#             print("DB connection Successfull!!")
#             break 
#         except Exception as e:
#             print("Could not connect to db")
#             print(e)
#             time.sleep(3)
