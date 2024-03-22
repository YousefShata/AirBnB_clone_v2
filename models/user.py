#!/usr/bin/python3
"""
User Model
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class User(BaseModel):
    """
    User Class
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
