#!/usr/bin/python3

"""unittest for base model"""

import unittest
import os
import uuid
import datetime
from models.base_model import BaseModel
from time import sleep


class TestBaseModel(unittest.TestCase):
    """ test base model """

    def setUp(self):
        """This method is called before each test method in the test class.
        """
        self.new_odj = BaseModel()
        self.new2_odj = BaseModel()

    def test_uuid_good_format(self):
        """
        Tests if UUID is in the correct format.
        """
        self.assertIsInstance(uuid.UUID(self.new_odj.id), uuid.UUID)

    def test_uuid_version(self):
        """
        Tests if the version of the UUID is 4
        """
        v_uuid = uuid.UUID(self.new_odj.id)

        self.assertEqual(v_uuid.version, 4)

    def test_str(self):
        """Testing __str__ method"""
        self.new_odj.id = "12"
        strForm = self.new_odj.__str__()
        expected = "[BaseModel] (12)"
        self.assertIn(expected, strForm)

    def test_different_uuid(self):
        """
        checks id UUID are different when different objects are created.
        """

        uuid_one = uuid.UUID(self.new_odj.id)
        uuid_two = uuid.UUID(self.new2_odj.id)

        self.assertNotEqual(uuid_one, uuid_two)

    def test_init(self):
        """ test instantiation type"""
        self.assertEqual(type(self.new_odj.id), str)
        self.assertEqual(type(self.new_odj.updated_at), datetime.datetime)
        self.assertEqual(type(self.new_odj.created_at), datetime.datetime)

    def test_save(self):
        """ test save method"""
        curr_time = self.new_odj.updated_at
        self.new_odj.save
        self.assertEqual(curr_time, self.new_odj.updated_at)
        """ test with arg"""
        with self.assertRaises(TypeError):
            self.new_odj.save(304)

    def test_methodDocsSave(self):
        """
        test basemodel save again for some reason
        """
        methodDoc = (
                __import__("models.base_model")
                .base_model.BaseModel.save.__doc__)
        self.assertGreater(len(methodDoc), 0)

    def test_to_dict(self):
        """test to_dict method"""
        self.new_odj.name = "bnb"
        self.new_odj.num = 10

        new_dic = self.new_odj.to_dict()
        self.assertEqual(type(new_dic['num']), int)
        self.assertEqual(type(new_dic['name']), str)
        self.assertEqual(type(new_dic['__class__']), str)
        self.assertEqual(new_dic['__class__'], 'BaseModel')
        self.assertEqual(type(new_dic['updated_at']), str)
        self.assertEqual(type(new_dic['id']), str)
        self.assertEqual(type(new_dic['created_at']), str)
        """ test with arg"""
        with self.assertRaises(TypeError):
            self.new_odj.to_dict('str')
        
    def test_moduleDocs(self):
        """
        test moduleDoc
        """
        moduleDoc = (
                __import__("models.base_model")
                .user.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        """
        test class Doc
        """
        classDoc = (
                __import__("models.base_model")
                .user.User.__doc__)
        self.assertGreater(len(classDoc), 0)

    def test_save_updatedAt(self):
        """test updating the public instance attribute updated_at
            with the current datetime"""
        new_inst = BaseModel()
        sleep(0.05)
        beforeSave_updated_at = new_inst.updated_at
        new_inst.save()
        self.assertNotEqual(beforeSave_updated_at, new_inst.updated_at)

    def test_save_BaseModel(self):
        """test if the save method works"""
        self.new_odj.save()
        self.assertNotEqual(self.new_odj.created_at, self.new_odj.updated_at)


if __name__ == '__main__':
    unittest.main()
