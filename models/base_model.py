#!/usr/bin/python3
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """INITIALIZING BaseModel.

        Args:
            *args (any): Unused.
            **kwargs(dict): Key pairs of attribtes."""
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for q, w in kwargs.items():
                if q == "created_at" or q == "updated_at":
                    self.__dict__[q] = datetime.strptime(w, tform)
                else:
                    self.__dict__[q] = w

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict

    def __str__(self):
        claname = self.__class__.__name__
        return "[{}] ({}) {}".format(claname, self.id, self.__dict__)
