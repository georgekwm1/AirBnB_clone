#!/usr/bin/python3
import unittest

""" Tests the BaseModel class"""
from models.place import Place


class TestPlace(Place, unittest.TestCase):
    pass
