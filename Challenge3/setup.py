from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///library6.db', echo=True)
Base = declarative_base()

########################################################################
class Library(Base):
    """"""
    __tablename__ = "library"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)
    renterID = Column(Integer)

    #----------------------------------------------------------------------
    def __init__(self, title, genre, author, renterID):
        """"""
        self.title = title
        self.genre = genre
        self.author = author
        self.renterID = renterID

# create tables
Base.metadata.create_all(engine)
