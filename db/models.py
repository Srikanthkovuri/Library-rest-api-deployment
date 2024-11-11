"""This module has database tables
"""
from sqlalchemy import Integer,String,Date,Column
from db.database import Base

class Books(Base):
    """This class has a table attributes

    Args:
        Base (class):pre-defined class
    """
    __tablename__="books"
    id=Column(Integer, primary_key=True, index=True)
    title=Column(String)
    author=Column(String)
    isbn=Column(String)
    published_date=Column(Date)
