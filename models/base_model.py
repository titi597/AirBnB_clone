#!/usr/bin/python3
"""defining base model."""
import models
import uuid
from datetime import datetime


class BaseModel:
    """representing base models."""

    def __init__(self, *args, **kwargs):
        """Initializing base models."""
        if kwargs:
            kwargs.pop('__class__', None)
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)
    def __str__(self):
        """Return the str representation of the BaseModel instance."""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updating updated_at with the current datetime."""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance."""

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
