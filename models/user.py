#!/usr/bin/python3
""" Defines User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """ The User class that inherits from BaseModel."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
