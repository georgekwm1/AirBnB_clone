#!/usr/bin/python3
"""Defines FileStorage class."""
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json


class FileStorage:
    """The FileStorage class."""

    __file_path = "storage.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        class_name = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[class_name] = obj

    def save(self):
        with open(FileStorage.__file_path, "w") as file:
            my_dict = FileStorage.__objects
            my_dict = {key: my_dict[key].to_dict() for key in my_dict.keys()}
            json.dump(my_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the file exists)"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
            for obj in data.values():
                class_name = obj["__class__"]
                self.new(eval(class_name)(**obj))

        except FileNotFoundError:
            pass  # File doesn't exist yet, no need to do anything

