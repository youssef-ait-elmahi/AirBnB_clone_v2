#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
import uuid

Base = declarative_base()


class BaseModel:
    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()

    def save(self):
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def delete(self):
        from models import storage
        storage.delete(self)

    def to_dict(self):
        dictionary = {**self.__dict__}
        dictionary.pop('_sa_instance_state', None)
        dictionary['__class__'] = self.__class__.__name__
        if self.created_at is not None:
            dictionary['created_at'] = self.created_at.strftime(
                '%Y-%m-%dT%H:%M:%S.%f')
        if self.updated_at is not None:
            dictionary['updated_at'] = self.updated_at.strftime(
                '%Y-%m-%dT%H:%M:%S.%f')
        return dictionary

    def delete(self):
        """Deletes the current instance from storage"""
        from models import storage
        storage.delete(self)
