#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, storage=None, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    setattr(
                            self,
                            key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                        )
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            if storage:
                storage.new(self)

    def __str__(self):
        cname = self.__class__.__name__
        return "[{}] ({}) {}".format(cname, self.id, self.__dict__)

    def save(self, storage=None):
        if storage is None:
            from models.engine.file_storage import FileStorage
            storage = FileStorage()
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
