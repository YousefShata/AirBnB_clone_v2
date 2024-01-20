#!/usr/bin/python3
"""test place class"""

import unittest
from models.base_model import BaseModel
from models.place import Place
import models.base_model
import models.place
import datetime


class TestPlace(unittest.TestCase):
    """ class to test city class """
    def setUp(self):
        """set up method"""
        self.new_obj = Place()

    def test_init_place(self):
        """ test instantiation of class """
        self.assertEqual(type(self.new_obj.id), str)
        self.assertEqual(type(self.new_obj.updated_at), datetime.datetime)
        self.assertEqual(type(self.new_obj.created_at), datetime.datetime)

    def test_save_place(self):
        """ test State.save() """
        current_updatedAt = self.new_obj.updated_at
        self.new_obj.save()
        self.assertNotEqual(current_updatedAt, self.new_obj.updated_at)

        """ test with args """
        with self.assertRaises(TypeError):
            self.new_obj.save(10)

    def test_to_dict_place(self):
        """ test BaseModel.to_dict() """
        self.new_obj.name = "bnb"
        dict_ = self.new_obj.to_dict()
        self.assertEqual(type(dict_['name']), str)
        self.assertEqual(type(dict_['__class__']), str)
        self.assertEqual(dict_['__class__'], "Place")
        self.assertEqual(type(dict_['updated_at']), str)
        self.assertEqual(type(dict_['id']), str)
        self.assertEqual(type(dict_['created_at']), str)
        """ test with args """
        with self.assertRaises(TypeError):
            self.new_obj.to_dict('str')
    
    def test_attributes_Type(self):
        """
        test place attribute
        """
        place = Place()
        self.assertIs(type(place.name), str)
        self.assertIs(type(place.city_id), str)
        self.assertIs(type(place.user_id), str)
        self.assertIs(type(place.description), str)
        self.assertIs(type(place.number_rooms), int)
        self.assertIs(type(place.number_bathrooms), int)
        self.assertIs(type(place.max_guest), int)
        self.assertIs(type(place.price_by_night), int)
        self.assertIs(type(place.latitude), float)
        self.assertIs(type(place.longitude), float)
        self.assertIs(type(place.amenity_ids), list)

    def test_moduleDocs(self):
        """
        test moduleDoc
        """
        moduleDoc = (
                __import__("models.place")
                .user.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        """
        test class Doc
        """
        classDoc = (
                __import__("models.place")
                .user.User.__doc__)
        self.assertGreater(len(classDoc), 0)


if __name__ == '__main__':
    unittest.main()
