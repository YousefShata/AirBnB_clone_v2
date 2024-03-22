#!/usr/bin/python3
"""
State Model
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """
    State Class
    """

    __tablename__ = "state"
    name = Column("name", String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        return self.cities 
