"""This module has database env
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

#loads environment variables.set default values if not present
load_dotenv()

DATABASE_URL=os.getenv('DATABASE_URL')

#creating an engine
engine=create_engine(DATABASE_URL)

#to connect to database
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base=declarative_base()
# to get the connetction with database
def get_db():
    """Get database connection

    Yields:
        : _description_
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

