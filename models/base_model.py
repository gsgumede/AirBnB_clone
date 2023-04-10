#!/usr/bin/python3
"""This module defines the BaseModel class"""

from datetime import datetime
import uuid


class BaseModel:
    """This class defines all common attributes/methods for other classes"""

    def __init__(self):
        """Initialisation

        Args:
        id (uuid): The uuid of an instance
        created_at (datetime): The current datatime
        updated_at (datetime): The current dattime updated
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        """Print [<class name>] (<self.id>) <self.__dict__> """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """Update the public instance attribute updated_at with current datetime"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Returns a dictionary containing all keys/values of _dict_ of the instance"""
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()

        return dict_copy


    