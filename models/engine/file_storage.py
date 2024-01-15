#!/usr/bin/python3
"""Defines FileStorage class."""
from models.base_model import BaseModel
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
        try:
            with open(FileStorage.__file_path, "r") as file:
                FileStorage.__objects = dict(json.load(file))
        except FileNotFoundError:
            pass
        
        my_dict = FileStorage.__objects
        for key in my_dict.keys():
            my_dict[key] = BaseModel(**my_dict[key])

        FileStorage.__objects = my_dict
