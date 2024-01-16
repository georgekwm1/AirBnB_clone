#!/usr/bin/python3
import unittest

""" Tests the BaseModel class"""
from models.review import Review


class TestReview(Review, unittest.TestCase):
    pass
