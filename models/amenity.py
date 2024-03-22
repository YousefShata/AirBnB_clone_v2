#!/usr/bin/python3
"""
Amenity Model
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Amenity(BaseModel):
    """
    Amenity Class
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
