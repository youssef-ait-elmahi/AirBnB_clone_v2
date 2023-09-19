#!/usr/bin/python3
"""This module contains a test class for testing the City class. """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """This class contains unit tests for the City class. """

    def __init__(self, *args, **kwargs):
        """Initialize the test class. """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test state_id attribute of City class. """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test name attribute of City class. """
        new = self.value()
        self.assertEqual(type(new.name), str)
