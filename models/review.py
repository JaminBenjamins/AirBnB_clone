#!/usr/bin/python3
""" This a class used in review by a user """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class for managin review objects
        Attributes:
            place_id (str): The ID of a location
            user_id (str): The ID of a user
            text (str): Information provided by user
    """

    place_id = ""
    user_id = ""
    text = ""
