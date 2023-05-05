#!/usr/bin/python3
"""Entry point of the command interpreter"""

import shlex
from models import storage
import re
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
import models
from models.base_model import BaseModel
from models.user import User
import cmd

def combine(obj, id):
    return f"{obj}.{id}"

classes_dict =  {"BaseModel": BaseModel,
             "User": User,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "State": State,
            "Review": Review}

class HBNBCommand(cmd.Cmd):

    prompt = "hbnb>"
    __classes = {
        "BaseModel"
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program if EOF is encountered"""
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("**class name missing**")
            return
        if arg not in classes_dict.keys():
            print("**class doesn't exist**")
            return
        new_obj = classes_dict[arg]()
        new_obj.save()
        print(new_obj.id)
    
    def do_show(self, arg):
        """Show representation of the class"""
        if not arg:
            print("**class name missing**")
            return
        names_list = arg.split(" ")
        if len(names_list) == 1:
            print("**instance id missing**")
            return
        class_name = names_list[0]
        class_id = names_list[1]
        if class_name not in classes_dict.keys():
            print("**class doesn't exist**")
            return
        objects_saved = storage.all()
        for k, v in objects_saved.items():
            if k == f"{class_name}.{class_id}":
                print(v)
                return
        print("**no instance found**")
    def do_destroy(self, arg):
        """Destroy an instance of BaseModel"""
        if not arg:
            print("**class name missing**")
            return
        name_list = arg.split(" ")
        if len(name_list) == 1:
            print("**instance id missing**")
            return
        if name_list[0] not in classes_dict.keys():
            print("**class doesn't exist**")
            return
        del storage.all()[f"{name_list[0]}.{name_list[1]}"]
    def do_update(self, arg):
        """Update the base class"""
        _input = shlex.split(arg)
        query = ""
        if len(_input) is 0:
            print("**class name is missing**")
            return
        if _input[0] not in classes_dict.keys():
            print("**class doesn't exist**")
            return
        if len(_input) is 1:
            print("**instance id missing**")
            return
        if len(_input) > 1:
            my_object = None
            query = f"{_input[0]}.{_input[1]}"
            if query not in storage.all().keys():
                print("** no istance found **")
                return
            if len(_input) is 2:
                print("** attribute name missing **")
                return
            if len(_input) is 3:
                print("** value missing **")
            for k, v in storage.all().keys():
                if query is k:
                    my_object = v
            setattr(my_object,_input[2], _input[3])
            storage.save()
            
if __name__ == "__main__":
    HBNBCommand().cmdloop()
