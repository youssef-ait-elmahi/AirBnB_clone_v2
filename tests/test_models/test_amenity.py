#!/usr/bin/python3
"""Unit tests for the Amenity class. """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test cases for the Amenity class."""

    def __init__(self, *args, **kwargs):
        """Initializes a new Amenity object."""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test that the name of the amenity is a string. """
        new = self.value()
        self.assertEqual(type(new.name), str)
