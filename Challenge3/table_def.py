# table_def.py
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///library.db', echo=True)
Base = declarative_base()
 
########################################################################
class Renter(Base):
    """"""
    __tablename__ = "renters"
 
    id = Column(Integer, primary_key=True)
    name = Column(String)  
 
    #----------------------------------------------------------------------
    def __init__(self, name):
        """"""
        self.name = name    
 
########################################################################
class Book(Base):
    """"""
    __tablename__ = "books"
 
    id = Column(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String)
    author = Column(String)
    renter = Column(Integer)

 
    #----------------------------------------------------------------------
    def __init__(self, title, genre, author, renter):
        """"""
        self.title = title
        self.genre = genre
        self.author = author
        self.renter = renter
 
# create tables
Base.metadata.create_all(engine)


