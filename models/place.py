#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from os import getenv
from sqlalchemy.orm import relationship


class Place(BaseModel, Base if (getenv("HBNB_TYPE_STORAGE") == "db") else object):
    """ A place to stay """
    if (getenv("HBNB_TYPE_STORAGE") == "db"):
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        review = relationship("Review", backref="place", cascade="delete")
        place_amenity = Table('place_amenity', Base.metadata, Column(
            'place_id', String(60), ForeignKey(
                'places.id'), primary_key=True, nullable=False),
            Column('amenity_id', String(60), ForeignKey(
                'amenities.id'), primary_key=True,
            nullable=False)
        )
        amenities = relationship(
            'Amenity', secondary="place_amenity", viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def review(self):
            """return the list of Review instance """
            from models import storage
            my_list = []
            for key, value in storage.__objects.items():
                if value.__class__ == 'Review' and self.id == value.place_id:
                    my_list.append(value)
            return my_list

        @property
        def amenities(self):
            """return the list of Amenity"""
            if len(self.amenity_ids) > 0:
                return self.amenity_ids

        @amenities.setter
        def amenities(self, value):
            """handles append method for adding an amenity id"""
            if value.__class__.__name__ == 'Amenity':
                self.amenity_ids.append(value)
