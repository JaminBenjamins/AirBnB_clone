#!/usr/bin/python3
"""This module defines unittests for models/state.py.

Unittest classes:
    TestStateInstantiation
    TestStateSave
    TestStateToDict
"""
import os
import unittest
from datetime import datetime
from time import sleep
from models.state import State
from models import storage


class TestStateInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def test_no_args_instantiates(self):
        self.assertIsInstance(State(), State)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), storage.all().values())

    def test_id_is_string(self):
        self.assertIsInstance(State().id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(State().created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(State().updated_at, datetime)

    def test_name_is_class_attribute(self):
        state = State()
        self.assertIsInstance(State.name, str)
        self.assertIn("name", dir(state))
        self.assertNotIn("name", state.__dict__)

    def test_two_states_unique_ids(self):
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_two_states_different_created_at(self):
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.created_at, state2.created_at)

    def test_two_states_different_updated_at(self):
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.updated_at, state2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        state = State()
        state.id = "123456"
        state.created_at = state.updated_at = dt
        state_str = state.__str__()
        self.assertIn("[State] (123456)", state_str)
        self.assertIn("'id': '123456'", state_str)
        self.assertIn("'created_at': " + dt_repr, state_str)
        self.assertIn("'updated_at': " + dt_repr, state_str)

    def test_args_unused(self):
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        state = State(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(state.id, "345")
        self.assertEqual(state.created_at, dt)
        self.assertEqual(state.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestStateSave(unittest.TestCase):
    """Unittests for testing save method of the State class."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        state = State()
        sleep(0.05)
        first_updated_at = state.updated_at
        state.save()
        self.assertLess(first_updated_at, state.updated_at)

    def test_two_saves(self):
        state = State()
        sleep(0.05)
        first_updated_at = state.updated_at
        state.save()
        second_updated_at = state.updated_at
        self.assertLess