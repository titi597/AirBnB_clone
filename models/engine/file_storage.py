#!/usr/bin/python3
"""filestorage."""
import json


class FileStorage:
    """the file that stores basemodels."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objs = {key: obj.to_dict() for key,
                           obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, val in data.items():
                    class_name, obj_id = key.split('.')
                    cls = BaseModel
                    self.__objects[key] = cls(**val)
        except FileNotFoundError:
            pass