#!/usr/bin/python3
"""Defines FileStorage class."""
import json


class FileStorage:
    """The FileStorage class."""

    __file_path = "storage.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        class_name = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[class_name] = obj.to_dict()

    def save(self):
        with open(FileStorage.__file_path, "w") as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as file:
                FileStorage.__objects = json.load(file)
        except FileNotFoundError:
            pass
