#Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances
#it will have this Private class attributes:
# __file_path: string - path to the JSON file (ex: file.json)
# __objects: dictionary - empty but will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)    
# Public instance methods:
# all(self): returns the dictionary __objects
# new(self, obj): sets in __objects the obj with key <obj class name>.id
# save(self): serializes __objects to the JSON file (path: __file_path)
# reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)

import json
import os
from models.base_model import BaseModel

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path )"""

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump({key: value.to_dict() for key, value in FileStorage.__objects.items()}, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects, if the JSON file exists.
        If the file doesn't exist, does nothing. No exception is raised.
        """

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                for key, value in json.load(file).items():
                    FileStorage.__objects[key] = BaseModel(**value)
        else:
            pass    # No exception should be raised if the file doesn't exist
