#!/usr/bin/python3
"""This module contains TestCases for the User class contained in
models/user.py.
"""


import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Testcase for the user class.
    """
    def test_inheritance(self):
        """tests if the User class inherits from the BaseModel class.
        """
        usr1 = User()
        self.assertTrue(issubclass(usr1.__class__, BaseModel))

    def test_public_attributes(self):
        """tests if the public class attributes are accessible.
        """
        usr1 = User()
        self.assertTrue(hasattr(usr1, "email"))
        self.assertTrue(hasattr(usr1, "password"))
        self.assertTrue(hasattr(usr1, "first_name"))
        self.assertTrue(hasattr(usr1, "last_name"))
