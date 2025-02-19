#!/usr/bin/python3
"""Test cases for the User class."""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ The first name should be a string """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ The last name should be a string """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ The email should be a string """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ The password should be a string """
        new = self.value()
        self.assertEqual(type(new.password), str)
