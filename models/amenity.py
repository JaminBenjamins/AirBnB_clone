#!/usr/bin/python3
""" This is a module creating the amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class for handling amenity objects
        Attributes:
            name (str): The amenity name
    """
    name = ""
