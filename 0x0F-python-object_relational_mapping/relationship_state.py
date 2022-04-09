#!/usr/bin/python3

"""
Create a base State in relation with city
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City

class State(Base):
    """Class : State
        
    Attribute:
        id (int)
        name (int)
        cities (list)
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
