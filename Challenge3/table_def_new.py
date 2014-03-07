# table_def.py
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///flood.db', echo=True)
Base = declarative_base()
 

########################################################################
class Shelter(Base):
    """"""
    __tablename__ = "shelters"
 
    id = Column(Integer, primary_key=True)
    address = Column(String)
    phone = Column(String)
    email = Column(String)
    beds = Column(String)
 
 
    #----------------------------------------------------------------------
    def __init__(self, address, phone, email, beds):
        """"""
        self.address = address
        self.phone = phone
        self.email = email
        self.beds = beds
 
# create tables
Base.metadata.create_all(engine)
