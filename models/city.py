#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """City class"""
    __tablename__ = 'cities'

    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    # Add the relationship with Place
    places = relationship(
        "Place", cascade="all, delete", back_populates="cities")
