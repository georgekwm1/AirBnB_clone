#!/usr/bin/python3
"""Defines the BaseModel class."""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """The BaseModel class."""

    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            to_time = datetime.strptime
            self.__dict__ = kwargs
            self.created_at = to_time(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = to_time(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__.pop("__class__", "Key not found")

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        my_dict = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                my_dict[key] = datetime.isoformat(value)
            else:
                my_dict[key] = value

        my_dict["__class__"] = __class__.__name__
        return my_dict

    def __str__(self):
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
