#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlaceInstantiation
    TestPlaceSave
    TestPlaceToDict
"""

import os
import unittest
from datetime import datetime
from time import sleep
from models.place import Place
from models import storage


class TestPlaceInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place Class."""

    def test_no_args_instantiates(self):
        self.assertIsInstance(Place(), Place)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), storage.all().value())

    def test_id_is_public_str(self):
        self.assertIsInstance(Place().id, str)

    def test_created_at_is_public_datetime(self):
        self.assertIsInstance(Place().created_at, datetime)

    def test_updated_at_is_public_datetime(self):
        self.assertIsInstance(Place().updated_at, datetime)

    def test_city_id_is_public_class_attribute(self):
        place = Place()
        self.assertIsInstance(Place.city_id, str)
        self.assertIn("city_id", dir(place))
        self.assertNotIn("city_id", place.__dict__)

    def test_user_id_is_public_class_attribute(self):
        place = Place()
        self.assertIsInstance(Place.user_id, str)
        self.assertIn("user_id", dir(place))
        self.assertNotIn("user_id", place.__dict__)

    def test_name_is_public_class_attribute(self):
        place = Place()
        self.assertIsInstance(Place.name, str)
        self.assertIn("name", dir(place))
        self.assertNotIn("name", place.__dict__)

    def test_description_is_public_class_attribute(self):
        place = Place()
        self.assertIsInstance(Place.description, str)
        self.assertIn("description", dir(place))
        self.assertNotIn("description", place.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        place = Place()
        self.assertIsInstance(Place.number_rooms, int)
        self.assertIn("number_rooms", dir(place))
        self.assertNotIn("number_rooms", place.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        place = Place()
        self.assertIsInstance(Place.number_bathrooms, int)
        self.assertIn("number_bathrooms", dir(place))
        self.assertNotIn("number_bathrooms", place.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        place = Place()
        self.assertIsInstance(Place.max_guest, int)
        self.assertIn("max_guest", dir(place))
        self.assertNotIn("max_guest", place.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        place = Place()
        self.assertIsInstance(Place.price_by_night, int)
        self.assertIn("price_by_night", dir(place))
        self.assertNotIn("price_by_night", place.__dict__)

    def test_latitude_is_public_class_attribute(self):
        place = Place()
        self.assertIsInstance(Place.latitude, float)
        self.assertIn("latitude", dir(place))
        self.assertNotIn("latitude", place.__dict__)

    def test_longitude_is_public_class_attribute(self):
        place = Place()
        self.assertIsInstance(Place.longitude, float)
        self.assertIn("longitude", dir(place))
        self.assertNotIn("longitude", place.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        place = Place()
        self.assertIsInstance(Place.amenity_ids, list)
        self.assertIn("amenity_ids", dir(place))
        self.assertNotIn("amenity_ids", place.__dict__)

    def test_two_places_unique_ids(self):
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_two_places
