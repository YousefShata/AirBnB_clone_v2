#!/usr/bin/python3
"""test amenity class"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import models.base_model
import models.amenity
import datetime


class TestAmenity(unittest.TestCase):
    """ class to test city class """
    def setUp(self):
        """This method is called before each test method in the test class.
        """
        self.new_obj = Amenity()

    def test_init_amenity(self):
        """ test instantiation of class """
        self.assertEqual(type(self.new_obj.id), str)
        self.assertEqual(type(self.new_obj.updated_at), datetime.datetime)
        self.assertEqual(type(self.new_obj.created_at), datetime.datetime)

    def test_save_amenity(self):
        """ test Amenity.save() """
        current_updatedAt = self.new_obj.updated_at
        self.new_obj.save()
        self.assertNotEqual(current_updatedAt, self.new_obj.updated_at)

        """ test with args """
        with self.assertRaises(TypeError):
            self.new_obj.save(13)

    def test_to_dict_amenity(self):
        """ test Amenity.to_dict() """
        self.new_obj.name = "NYC"
        dict_ = self.new_obj.to_dict()
        self.assertEqual(type(dict_['name']), str)
        self.assertEqual(type(dict_['__class__']), str)
        self.assertEqual(dict_['__class__'], "Amenity")
        self.assertEqual(type(dict_['updated_at']), str)
        self.assertEqual(type(dict_['id']), str)
        self.assertEqual(type(dict_['created_at']), str)
        """ test with args """
        with self.assertRaises(TypeError):
            self.new_obj.to_dict('str')

    def test_moduleDocs(self):
        """
        test moduleDoc
        """
        moduleDoc = (
                __import__("models.amenity")
                .user.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_name_Type(self):
        """
        test class attribute
        """
        amenity = Amenity()
        self.assertIs(type(amenity.name), str)

    def test_classDocs(self):
        """
        test class Doc
        """
        classDoc = (
                __import__("models.amenity")
                .user.User.__doc__)
        self.assertGreater(len(classDoc), 0)


if __name__ == '__main__':
    unittest.main()
