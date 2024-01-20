#!/usr/bin/python3
"""test review class"""

import unittest
from models.base_model import BaseModel
from models.review import Review
import models.base_model
import models.review
import datetime


class TestReview(unittest.TestCase):
    """ class to test city class """
    def setUp(self):
        """set up method"""
        self.new_obj = Review()

    def test_init_review(self):
        """ test instantiation of class """
        self.assertEqual(type(self.new_obj.id), str)
        self.assertEqual(type(self.new_obj.updated_at), datetime.datetime)
        self.assertEqual(type(self.new_obj.created_at), datetime.datetime)

    def test_save_review(self):
        """ test Review.save() """
        current_updatedAt = self.new_obj.updated_at
        self.new_obj.save()
        self.assertNotEqual(current_updatedAt, self.new_obj.updated_at)
        """ test with args """
        with self.assertRaises(TypeError):
            self.new_obj.save(10)

    def test_to_dict_review(self):
        """ test Review.to_dict() """
        self.new_obj.text = "bnb"
        dict_ = self.new_obj.to_dict()
        self.assertEqual(type(dict_['text']), str)
        self.assertEqual(type(dict_['__class__']), str)
        self.assertEqual(dict_['__class__'], "Review")
        self.assertEqual(type(dict_['updated_at']), str)
        self.assertEqual(type(dict_['id']), str)
        self.assertEqual(type(dict_['created_at']), str)
        """ test with args """
        with self.assertRaises(TypeError):
            self.new_obj.to_dict('str')

    def test_attributes_Type(self):
        """
        test attribute type
        """
        review = Review()
        self.assertIs(type(review.text), str)
        self.assertIs(type(review.place_id), str)
        self.assertIs(type(review.user_id), str)

    def test_moduleDocs(self):
        """
        test moduleDoc
        """
        moduleDoc = (
                __import__("models.review")
                .user.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        """
        test class Doc
        """
        classDoc = (
                __import__("models.review")
                .user.User.__doc__)
        self.assertGreater(len(classDoc), 0)


if __name__ == '__main__':
    unittest.main()
