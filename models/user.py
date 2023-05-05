#!/user/bin/python3
"""This module defines the class User"""
from models.base_model import BaseModel

class User(BaseModel):
    """User class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email =""
        self.password = ""
        self.firstname = ""
        self.lasname= ""
        
