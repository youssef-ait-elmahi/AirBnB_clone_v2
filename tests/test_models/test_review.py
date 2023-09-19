#!/usr/bin/python3
"""This module contains a test class for testing the Review class. """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """This class contains unit tests for the Review class. """

    def __init__(self, *args, **kwargs):
        """Initialize the test class. """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test place_id attribute of Review class. """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Test user_id attribute of Review class. """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Test text attribute of Review class. """
        new = self.value()
        self.assertEqual(type(new.text), str)
