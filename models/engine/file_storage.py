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
            for (keyA, valueA), (keyC, valueC), (keyP, valueP), (keyR, valueR), (keyS, valueS), (keyU, valueU) in zip(Amenity.__dict__.items(), City.__dict__.items(), Place.__dict__.items(), Review.__dict__.items(), State.__dict__.items(), User.__dict__.items()) :
                
                my_dict[keyA] = valueA
                my_dict[keyC] = valueC
                if keyC == "state_id":
                    valueC = State.id

                my_dict[keyP] = valueP
                if keyP == "city_id":
                    valueP = City.id
                if keyP == "user_id":
                    valueP = User.id
                if keyP == "amenity_ids":
                    valueP = Amenity.id

                my_dict[keyR] = valueR
                if keyR == "place_id":
                    valueR = City.id
                if keyR == "user_id":
                    valueR = User.id
                    
                my_dict[keyS] = valueS
                my_dict[keyU] = valueU
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
