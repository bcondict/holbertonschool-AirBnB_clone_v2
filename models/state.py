#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base if (getenv("HBNB_TYPE_STORAGE") == "db") else object):
    """ State class """
    if (getenv("HBNB_TYPE_STORAGE") == "db"):
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cites = relationship("City", backref="state", cascade="delete")
    else:
        name = ""

        @property
        def cities(self):
            """ return a list of City instances"""
            from models import storage
            my_list = []
            for key, value in storage.__objects.items():
                if value.__class__ == 'City' and self.id == value.state_id:
                    my_list.append(value)
            return my_list

