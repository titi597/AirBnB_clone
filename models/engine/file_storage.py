#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User  # Add User import


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to __objects."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON and save to file."""
        se_object = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(se_object, file)

    def reload(self):
        """Deserialize JSON from file and load into __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                for key, obj_dict in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    # Dynamically create objects for both BaseModel and User
                    if class_name == "BaseModel":
                        obj = BaseModel(**obj_dict)
                    elif class_name == "User":
                        obj = User(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
