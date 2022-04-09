#!/usr/bin/python3

"""
Create the city class database
"""

from sqlalchemy import ForeignKey
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Class : Cities"""

    __tablename__ = "cities"
    id = Column(
        Integer, autoincrement=True, unique=True,
        nullable=False, primary_key=True
    )
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False,
    )
