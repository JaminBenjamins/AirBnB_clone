#!/usr/bin/python3
""" The class defines a geographical location """
from models.base_model import BaseModel


class State(BaseModel):
    """ Class for managing objects defined
    Attributes:
        name (str): Name of the state
    """

    name = ""
