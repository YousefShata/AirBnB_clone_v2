#!/usr/bin/python3
"""
File storage model for serialize and deserialize JSON files
"""
import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    FireStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        return the object file
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        set a new object
        """
        key = f"{obj.__class__.__name__}.{obj.id}"

        FileStorage.__objects[key] = obj

    def save(self):
        """
        serialize to json
        """
        serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()
        json_str = json.dumps(serialized_objects)
        with open(FileStorage.__file_path, "w") as Myfile:
            Myfile.write(json_str)

    def reload(self):
        """
        Deserialize from json
        """
        all_classes = [
                "BaseModel", "User", "Place", "State",
                "City", "Amenity", "Review"]
        if (path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as Myfile:
                json_string = Myfile.read()
                data = json.loads(json_string)
            for key, value in data.items():
                class_name = value['__class__']
                if class_name in all_classes:
                    obj = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj
