#!/usr/bin/python3
# This class defines the place where amenities and user are located
from models.base_model import BaseModel


class Place(BaseModel):
    """ Class for managing objects in specific location
        Attributes:
            city_id (str): The ID of the city
            user_id (str): The ID of a user
            name (str): The name of a user
            description (str): Description of a place
            number_rooms (int): the number of rooms of a place
            number_bathrooms (int): Washrooms present in a place
            max_guest (int): The capacity a place can hold
            price_by_night (int): Night price for staying at a place
            latitude (float): The x-coordinates of a place
            longitude (float): The y-coordinate of a place
            amenity_ids (list): Unique identifier of a place
        """

    city_id = ""
    user_id = ""
    name = ""
    descrption = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
