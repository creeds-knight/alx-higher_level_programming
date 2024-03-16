#!/usr/bin/python3
"""
    A module containing the class state and Instance of Base
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.format("root",
                       "root", "3306", "my_db"), pool_pre_ping=True)

Base = declarative_base()


class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
