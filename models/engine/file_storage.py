#!/usr/bin/python3
"""Define the FileStorage class."""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City

class FileStorage:
    """serializes instances to a JSON file
    and  to instances.
    """



    __file_path = "file.json"
    __objects = {}



    def all(self):
        """returns the dictionary."""
        return self.__objects

    def new(self, obj):
        """sets in __objects the  <obj class name>.id"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serialize __objects JSON file __file_path."""
        obj_of_dict = {}

        for key, obj in self.__objects.items():
            obj_of_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(obj_of_dict, f)

        """add by mr-You task 5 """


        
    def reload(self):
        """  (__file_path) exists);
        otherwise, do nothing. If the file doesnot exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r') as f:
                new_obj_of_dict = json.load(f)
            for value in new_obj_of_dict.values():
                class_Name = value["__class__"]
                self.new(eval(class_Name)(**value))
        except FileNotFoundError:
            pass
