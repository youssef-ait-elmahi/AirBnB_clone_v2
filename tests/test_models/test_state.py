#!/usr/bin/python3
"""This module contains a test class for testing the State class. """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """This class contains unit tests for the State class. """

    def __init__(self, *args, **kwargs):
        """Initialize the test class. """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test name attribute of State class. """
        new = self.value()
        self.assertEqual(type(new.name), str)
