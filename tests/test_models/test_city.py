#!/usr/bin/python3
"""test city class"""

import unittest
from models.base_model import BaseModel
from models.city import City
import models.base_model
import models.city
import datetime


class TestCity(unittest.TestCase):
    """ class to test city class """
    def setUp(self):
        """set up method"""
        self.new_obj = City()

    def test_init_city(self):
        """ test instantiation of class """
        self.assertEqual(type(self.new_obj.id), str)
        self.assertEqual(type(self.new_obj.updated_at), datetime.datetime)
        self.assertEqual(type(self.new_obj.created_at), datetime.datetime)

    def test_save_city(self):
        """ test State.save() """
        current_updatedAt = self.new_obj.updated_at
        self.new_obj.save()
        self.assertNotEqual(current_updatedAt, self.new_obj.updated_at)

        """ test with args """
        with self.assertRaises(TypeError):
            self.new_obj.save(10)

    def test_to_dict_city(self):
        """ test City.to_dict() """
        self.new_obj.name = "bnb"
        dict_ = self.new_obj.to_dict()
        self.assertEqual(type(dict_['name']), str)
        self.assertEqual(type(dict_['__class__']), str)
        self.assertEqual(dict_['__class__'], "City")
        self.assertEqual(type(dict_['updated_at']), str)
        self.assertEqual(type(dict_['id']), str)
        self.assertEqual(type(dict_['created_at']), str)
        """ test with args """
        with self.assertRaises(TypeError):
            self.new_obj.to_dict('str')

    def test_data_Type(self):
        """
        test City data types
        """
        city = City()
        self.assertIs(type(city.name), str)
        self.assertIs(type(city.state_id), str)

    def test_moduleDocs(self):
        """
        test moduleDoc
        """
        moduleDoc = (
                __import__("models.city")
                .user.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        """
        test class Doc
        """
        classDoc = (
                __import__("models.city")
                .user.User.__doc__)
        self.assertGreater(len(classDoc), 0)


if __name__ == '__main__':
    unittest.main()
