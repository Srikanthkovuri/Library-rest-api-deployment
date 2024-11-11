"""This module describes about Library api 
"""
from typing import List
from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from api.models import BookReq,BookRes
from db.database import get_db,Base,engine
from db.models import Books

Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.get("/")
def hello() -> dict[str, str]:
    """This function simply prints message body

    Returns:
        _type_: _description_
    """
    return {"messge":"Hello Srikanth"}

@app.get("/books",response_model=list[BookRes])
def get_books(db: Session=Depends(get_db)) -> List[Books]:
    """This function returns the books

    Args:
        request (BookReq): user-defined class with args
    """
    return db.query(Books).all()
    

@app.post("/books",response_model=BookRes)
def create_book(request: BookReq, db: Session=Depends(get_db)) -> Books:
    """This function creates a book by taking inputs from user

    Args:
        request (BookReq): user-defined class with args
    """
    db_books=Books(**request.model_dump())
    db.add(db_books)
    db.commit()
    db.refresh(db_books)
    return db_books

@app.get("/books/{book_id}", response_model=BookRes)
def get_book(book_id: int, db: Session = Depends(get_db)) -> Books | None:
    """This method gets a book
    """
    return db.query(Books).filter(Books.id == book_id).first()

@app.put("/books/{book_id}", response_model=BookRes)
def update_book(book_id: int, request: BookReq, db: Session = Depends(get_db)) -> Books | None:
    """This method updates a book
    """
    db_book= db.query(Books).filter(Books.id == book_id).first()
    if db_book:
        db_book.title = request.title
        db_book.author = request.author
        db_book.isbn = request.isbn
        db_book.published_date = request.published_date
        db.commit()
        db.refresh(db_book)
    return db_book


@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)) -> dict[str, str]:
    """This method deletes a book
    """
    db_book: Books | None = db.query(Books).filter(Books.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return {"message": "Book deleted successfully"}
