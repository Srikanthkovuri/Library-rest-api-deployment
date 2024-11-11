"""This module has neccessary classes
"""
from datetime import date
from pydantic import BaseModel,Field

class BookReq(BaseModel):
    """It has __class_vars__

    Args:
        BaseModel (class): pre-defined class
    """
    title: str = Field(...,description="This Sherlock Holmes mystery involves a secret pact among four convicts",example="Beneath Mystery")
    author: str = Field(...,description="author name",example="SRIKANTH")
    isbn: str = Field(...,description="isbn number",example="7569889785")
    published_date: date

class BookRes(BaseModel):
    """It has __class_vars__

    Args:
        BaseModel (class): pre-defined class
    """
    id: int=Field(...,description="id",example="1001")
    title: str = Field(...,description="This Sherlock Holmes mystery involves a secret pact among four convicts",example="Beneath Mystery")
    author: str = Field(...,description="author name",example="SRIKANTH")
    isbn: str = Field(...,description="isbn number",example="7569889785")
    published_date: date
    class Config:
        orm_mode = True
