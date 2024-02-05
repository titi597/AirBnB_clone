#!/usr/bin/python3
"""a class BaseModel that defines all common attributes/methods."""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Representing the basemodel."""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        aptname = self.__class__.__name__
        return "[{}] ({}) {}".format(aptname, self.id, self.__dict__)
