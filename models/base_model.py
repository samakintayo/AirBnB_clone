#!/usr/bin/python3
"""This is a module that contains the BaseModel class definition.
"""


import uuid
import datetime


class BaseModel:
    """The class BaseModel defines all common attributes/methods
    for other classes created in this package.
    """

    def __init__(self):
        """Initializer/Constructor of the BaseModel class.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns the string representation of the BaseModel class,
        "[<class name>] (<self.id>) <self.__dict__>".
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute `updated_at` with the
        current datetime.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the `__dict__`
        of the instance.
        """
        instance_dict = {**self.__dict__, '__class__': self.__class__.__name__}
        if 'created_at' in instance_dict:
            instance_dict['created_at'] = self.created_at.isoformat()
        if 'updated_at' in instance_dict:
            instance_dict['updated_at'] = self.updated_at.isoformat()

        return instance_dict
