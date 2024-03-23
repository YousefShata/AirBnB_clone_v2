#!/usr/bin/python3
"""
This is the Base Model for all other classes
"""
import uuid
from datetime import datetime
import models
from sqlalchemy import Column, Integer, String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class BaseModel:
    """
    BaseModel Class which will be inharited
    """

    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    def __init__(self, *args, **kwargs):
        """
        Initiate instances attributes
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = str(value)
                elif key == "created_at":
                    value = datetime.fromisoformat(value)
                    self.created_at = value
                elif key == "updated_at":
                    value = datetime.fromisoformat(value)
                    self.updated_at = value
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Representing the object
        """
        name = type(self).__name__

        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """
        save the instance data
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        """
        dic = self.__dict__.copy()
        dic["__class__"] = type(self).__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()

        return dic

    def delete(self):
        """
        delete instance from storage
        """
        model.storage.delete(self)
