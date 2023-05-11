#!/usr/bin/python3
""" This module creates a user class """
from models.base _model import BaseModel


class User(BaseModel):
    """ Class managing user objectives
        Attributes:
            email (str): The mail of a user
            password (str): Password of a user
            first_name (str): Name of user
            last_name (str): The last name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
