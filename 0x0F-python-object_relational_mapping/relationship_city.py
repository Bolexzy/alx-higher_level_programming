#!/usr/bin/python3
"""Defines a City model.
Inherits from SQLAlchemy Base and links to the MySQL table states.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents a city for a MySQL database.

    params:
      __tablename__ (str): The name of the MySQL table to store cities.
      id (sqlalchemy.Integer): The citie's id.
      name (sqlalchemy.String): The citie's name.
      state_id (sqlalchemy.String): The city's state id.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
