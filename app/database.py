from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

# 'postgresql://<username>:<password>@localhost/<database_name>
SQL_ALQUEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

# Starting point for any SQL Alchemy application
engine = create_engine(SQL_ALQUEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Returns a class, and later, we will inherit from this class to create each of the database models or classes (the ORM models)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# region Database Connection
# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
#                                 password='mapajos2010', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print(
#             "\033[94m" + "DATABASE:" + "\033[0m" + " Database connection was succesfull!")
#         break
#     except Exception as error:
#         print("\033[91m" + "DATABASE:" + "\033[0m" +
#               " Attempting to connect to database...")
#         print("Error: ", error)
#         time.sleep(2)
# endregion
