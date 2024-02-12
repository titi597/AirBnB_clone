#!/usr/bin/python3
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objs = {
            key: obj.to_dict()
            for key, obj in self.__objects.items()
        }
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, val in data.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    self.__objects[key] = cls(**val)
        except FileNotFoundError:
            pass

    def classes(self):
        """Returns a list of class names stored in __objects."""
        return [cls.split('.')[0] for cls in self.__objects.keys()]
