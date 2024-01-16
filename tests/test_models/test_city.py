#!/usr/bin/python3
import unittest

""" Tests the BaseModel class"""
from models.city import City


class TestCity(City, unittest.TestCase):
    pass
