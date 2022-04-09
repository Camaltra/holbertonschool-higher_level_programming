#!/usr/bin/python3

"""
Create a base State in relation with city
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """Class : State"""

    __tablename__ = "states"
    id = Column(
        Integer, autoincrement=True, unique=True,
        nullable=False, primary_key=True
    )
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
