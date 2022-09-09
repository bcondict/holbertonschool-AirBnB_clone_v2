#!/usr/bin/python3
""" This module defines a class to manage data base storage for hbnb clone"""

from curses.ascii import US
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session


class DBStorage:
    """ This class manages all database stororage for hbnb clone"""
    __session = None
    __engine = None

    def __init__(self):
        """ Init method for data base storage"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        datebase = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}:{}".format(user, pwd, host, datebase), pool_pre_ping=True)
        metadata = MetaData()
        if getenv('HBNB_ENV') == 'test':
            metadata.drop_all()

    def all(self, cls=None):
        """ return a dictionary of all classes"""
        self.__session = Session(self.__engine)
        my_dict = dict()
        if cls == None:
            from models.amenity import Amenity
            from models.city import City
            from models.place import Place
            from models.review import Review
            from models.state import State
            from models.user import User

            list_cls = [Amenity, City, Place, Review, State, User]
            for querry_cls in list_cls:
                for querry_cls in self.__session.query(cls).all():
                    my_dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj

        else:
            for obj in self.__session.query(cls).all():
                my_dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        from models.base_model import BaseModel, Base
        from sqlalchemy.orm import sessionmaker, scoped_session

        Base.metadata.create_all(self.__engine)
        my_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        sc_session = scoped_session(my_session)
        self.__session = sc_session()
