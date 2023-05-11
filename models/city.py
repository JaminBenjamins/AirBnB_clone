#!/usr/bin/python3
""" This module creates a class city """
from models.base_model import BaseModel


class City(BaseModel):
    """ A module that creates a class defining location
        Attributes:
            state_id (str): The ID of a state
            name (str): The name of a city
    """
    state_id = ""
    name = ""
