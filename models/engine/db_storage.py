#!/usr/bin/python3
"""
DBStorage Module
"""
from sqlalchemy import (create_engine)
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """DBStorage class"""

    __engine = None
    __session = None

    user = os.getenv('HBNB_MYSQL_USER')
    password = os.getenv('HBNB_MYSQL_PWD')
    host = os.getenv('HBNB_MYSQL_HOST')
    database = os.getenv('HBNB_MYSQL_DB')
    env = os.getenv('HBNB_ENV')

    def __init__(self):
        """initate DB"""

        self.__engine = create_engine(
               'mysql+mysqldb://{}:{}@{}/{}'
               .format(self.user,
                       self.password,
                       self.host,
                       self.database),
               pool_pre_ping=True)

        if self.env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """return all data"""
        
        all_classes = [State, City]
        cls_dict = {}
        if cls is None:
            for entry in all_classes:
                for records in self.__session.query(entry).all():
                    className = records.__class__.__name__
                    key = className+ "." + records.id
                    cls_dict[key] = records
        else:
                for records in self.__session.query(cls).all():
                    className = records.__class__.__name__
                    key = className+ "." + records.id
                    cls_dict[key] = records

        return cls_dict

    def new(self, obj):
        """adda  new record"""
        
        if obj:
            self.__session.add(obj)

    def save(self):
        """ save all records"""

        self.__session.commit()

    def delete(self, obj=None):
        """ delete a record"""
        
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create session and tables"""
        
        Base.metadata.create_all(self.__engine)
        session_factory = scoped_session(
                sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = session_factory

