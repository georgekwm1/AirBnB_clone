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
            classes = [Amenity, BaseModel, City, Place, Review, State, User]
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
        """Deserializes the JSON file to __objects (only if the file exists)"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            for key, value in data.items():
                obj_key = key.split('.')
                class_name = obj_key[0]
                obj_id = obj_key[1]
                cls = eval(class_name)
                obj = cls(**value)
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass  # File doesn't exist yet, no need to do anything
        except json.decoder.JSONDecodeError:
            pass  # Handle the case where the file is empty or contains invalid JSON

        
        my_dict = FileStorage.__objects
        for key in my_dict.keys():
            my_dict[key] = BaseModel(**my_dict[key])

        FileStorage.__objects = my_dict
