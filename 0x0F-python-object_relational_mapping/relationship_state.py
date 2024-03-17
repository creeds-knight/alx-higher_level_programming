#!/usr/bin/python3
"""
    A module containing the class state and Instance of Base
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City
Base = declarative_base()


class State(Base):
    """ A class state to map to the table name states """
    __tablename__ = "states"

    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column('name', String(128), nullable=False)

    cities = relationship('City', back_populates="state",\
            cascade="all, delete-orphan", order_by=City.id)
