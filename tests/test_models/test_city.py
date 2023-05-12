#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity(unittest.TestCase):
    """Unittests for testing City class."""

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_instantiation(self):
        """Tests instantiation of City class."""
        cy = City()
        self.assertEqual(City, type(cy))
        self.assertIn(cy, models.storage.all().values())
        self.assertEqual(str, type(cy.id))
        self.assertEqual(datetime, type(cy.created_at))
        self.assertEqual(datetime, type(cy.updated_at))
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cy))
        self.assertNotIn("state_id", cy.__dict__)
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cy))
        self.assertNotIn("name", cy.__dict__)
        cy1 = City()
        cy2 = City()
        self.assertNotEqual(cy1.id, cy2.id)
        self.assertLess(cy1.created_at, cy2.created_at)
        self.assertLess(cy1.updated_at, cy2.updated_at)
        dt = datetime.today()
        dt_repr = repr(dt)
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        cystr = cy.__str__()
        self.assertIn("[City] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dt_repr, cystr)
        self.assertIn("'updated_at': " + dt_repr, cystr)
        cy = City(None)
        self.assertNotIn(None, cy.__dict__.values())
        dt_iso = dt.isoformat()
        cy = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(cy.id, "345")
        self.assertEqual(cy.created_at, dt)
        self.assertEqual(cy.updated_at, dt)
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_save(self):
        """Tests save method of City class."""
        cy = City()
        first_updated_at = cy.updated_at
        sleep(0.05)
        cy.save()
        self.assertLess(first_updated_at, cy.updated_at)
        first_updated_at = cy.updated_at
        sleep(0.05)
        cy.save()
        self.assertLess(first_updated_at, cy.updated_at)
        with self.assertRaises(TypeError):
            cy.save(None)
        cy.save()
        cyid = "City." + cy.id
        with open("file.json", "r") as f:
            self.assertIn(cyid, f.read())

    def test_to_dict(self):
        """Tests to_dict method of City class."""
        cy = City()
        self.assertTrue(dict, type(cy.to_dict()))
        self.assertIn("id", cy.to_dict())
        self.assertIn("created_at", cy.to_dict())
        self.assertIn("updated_at", cy.to_dict())
        self.assertIn("__class__", cy.to_dict())
        cy.middle_name = "School"