from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Place your database schema code here

# Example code:
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    flavors = relationship("Flavor")
    username = Column(String)
    email = Column(String)


class Flavor(Base):
    __tablename__ = "flavors"
    id = Column(Integer, primary_key = True)
    parent_id = Column(Integer, ForeignKey('user.id'))
    ingridents = Column(String)
    name = Column(String)

    def __repr__(self):
        return ("  {} is a ice cream flavor that contains:{}".format(self.name, self.ingridents))