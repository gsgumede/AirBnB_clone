#!/usr/bin/python3
"""Defines the class FileStorage"""

from models.base_model import BaseModel
import json


class FileStorage:
    """Serializes instances to JSON file and deserialises JSON file to instances"""

    def __init__(self):
        """Initialisation

        Args
        __file_path (str): file path
        __objects (dict): dictionary with key/value pairs of class name/object 
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects with <key class.name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serializes the objects to JSON file"""
        dict_copy = {}
        for k, v in self.__objects.items():
            dict_copy[k] = v.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as contents:
            json.dump(dict_copy, contents)
            

    def reload(self):
        """Deserializes the JSON file"""
        classes = {
            "BaseModel": BaseModel
        }
        json_dict = {}
        try:
            with open(self.__file_path, "r") as objs:
                json_dict = json.load(objs)
            for k, v in json_dict.items():
                for key, value in classes.items():
                    print(json_dict[k]["__class__"] )
                    if json_dict[k]["__class__"] == key:
                        self.new(classes[key](**json_dict[k]))
        except:
            pass
