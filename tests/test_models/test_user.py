#!/usr/bin/python3
"""test user class"""
import unittest
from models.base_model import BaseModel
from models.user import User
import models.base_model
import models.user
import inspect
import datetime


class TestUser(unittest.TestCase):
    """ class to test user class """
    def setUp(self):
        """set up method"""
        self.new_obj = User()

    def check_attributes(self):
        """ check for attributes """
        user = User()
        user.first_name = "bnb"
        user.last_name = "bnb"
        user.email = "bnb@email.com"
        user.password = "root"
        self.assertEqual(user.first_name, "bnb")
        self.assertEqual(user.last_name, "bnb")
        self.assertEqual(user.email, "bnb@email.com")
        self.assertEqual(user.password, "root")
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "email"))
        self.assertEqual(type(User.email), str)
        self.assertEqual(type(User.first_name), str)
        self.assertEqual(type(User.last_name), str)
        self.assertEqual(type(User.password), str)

    def test_init_user(self):
        """ test instantiation of class """
        self.assertEqual(type(self.new_obj.id), str)
        self.assertEqual(type(self.new_obj.updated_at), datetime.datetime)
        self.assertEqual(type(self.new_obj.created_at), datetime.datetime)

    def test_save_user(self):
        """ test User.save() """
        current_updatedAt = self.new_obj.updated_at
        self.new_obj.save()
        self.assertNotEqual(current_updatedAt, self.new_obj.updated_at)
        """ test with args """
        with self.assertRaises(TypeError):
            self.new_obj.save(10)

    def test_to_dict_city(self):
        """ test User.to_dict() """
        self.new_obj.first_name = "bnb"
        self.new_obj.last_name = "bnb"
        self.new_obj.email = "jonas@example.com"
        self.new_obj.password = "root"
        dict_ = self.new_obj.to_dict()
        self.assertEqual(type(dict_['first_name']), str)
        self.assertEqual(dict_['first_name'], "bnb")
        self.assertEqual(dict_['last_name'], "bnb")
        self.assertEqual(dict_['email'], "jonas@example.com")
        self.assertEqual(dict_['password'], "root")
        self.assertEqual(type(dict_['__class__']), str)
        self.assertEqual(dict_['__class__'], "User")
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
                __import__("models.user")
                .user.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        """
        test class Doc
        """
        classDoc = (
                __import__("models.user")
                .user.User.__doc__)
        self.assertGreater(len(classDoc), 0)


if __name__ == '__main__':
    unittest.main()
