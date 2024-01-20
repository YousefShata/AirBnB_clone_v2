#!/usr/bin/python3
"""test file storage"""
import unittest
from models.engine.file_storage import FileStorage
import models.engine.file_storage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """ test file storage class """

    def test_save_reload(self):
        """ test save(), reload(), all() functions """
        my_model = BaseModel()
        my_model.save()
        storage = FileStorage()
        self.assertTrue(os.path.exists('file.json'))

        """ load json file"""
        storage.reload()
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertTrue(isinstance(obj, BaseModel))

        """ adding positional args """
        with self.assertRaises(TypeError):
            my_model.save('str')
        with self.assertRaises(TypeError):
            storage.reload('str')
        with self.assertRaises(TypeError):
            storage.all('str')

    def test_all_return_dict(self):
        """Test all method that returns the dictionary __objects"""
        dict_of_obj = FileStorage._FileStorage__objects
        self.assertIsInstance(dict_of_obj, dict)

    def test_all_dict_of_obj(self):
        """Test if returns dict of obj"""
        dict_obj = FileStorage._FileStorage__objects
        for key, obj in dict_obj.items():
            self.assertIsInstance(obj, object)

    def test_new(self):
        """sets in __objects the obj with key <obj class name>.id"""
        new_base = BaseModel()
        self.assertIn("BaseModel." + new_base.id, models.storage.all().keys())

    def test_save(self):
        """Test serialization"""
        base_inst = BaseModel()
        models.storage.new(base_inst)
        models.storage.save()
        text = ""
        with open("file.json", "r") as fi:
            text = fi.read()
            self.assertIn("BaseModel." + base_inst.id, text)

    def test_reload(self):
        """Test Deserialization"""
        base_ = BaseModel()
        models.storage.new(base_)
        models.storage.save()
        models.storage.reload()
        dict_obj = FileStorage._FileStorage__objects
        self.assertIn(f"BaseModel." + base_.id, dict_obj)

    def test_moduleDocs(self):
        """
        Test Filestorage doc 
        """
        moduleDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        """
        test class doc
        """
        classDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.FileStorage.__doc__)
        self.assertGreater(len(classDoc), 0)

    def test_methodDocsSave(self):
        """
        test method save
        """
        methodDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.FileStorage.save.__doc__)
        self.assertGreater(len(methodDoc), 0)

if __name__ == "__main__":
    unittest.main()
