#!/usr/bin/python3
"""Defines FileStorage class."""
from models.base_model import BaseModel
from city import City
from amenity import Amenity
from place import Place
from review import Review
from state import State
from user import User
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
            classes = [Amenity, City, Place, Review, State, User]
            for cls in classes:
                for key, value in cls.to_dict().items():
                    if key == 'state_id':
                        value = f"{cls.__name__}.{cls.id}"
                    if key == 'city_id':
                        value = f"{cls.__name__}.{cls.id}"
                    if key == 'user_id':
                        value = f"{cls.__name__}.{cls.id}"
                    if key == 'amenity_ids':
                        value = f"{cls.__name__}.{cls.id}"
                    if key == 'place_id':
                        value = f"{cls.__name__}.{cls.id}"
                    if key == 'user_id':
                        value = f"{cls.__name__}.{cls.id}"
                    
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
