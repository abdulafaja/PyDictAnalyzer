import unittest

from pydictanalyzer.database import Database
from pydictanalyzer.exceptions import DatabaseException


class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        self.db = Database('sqlite://')

        self.obj_path = '/test/path'
        self.obj_type = 't'
        self.obj_size = 15
        self.obj = self.db.create_object(path=self.obj_path, type=self.obj_type, size=self.obj_size)

    def assertObjectEqual(self, object, another):
        self.assertEqual(object.id, another.id)
        self.assertEqual(object.path, another.path)
        self.assertEqual(object.type, another.type)
        self.assertEqual(object.size, another.size)

    def test_invalid_dialect_connection(self):
        self.assertRaises(DatabaseException, Database, 'invalid://')

    def test_create_object(self):
        session_obj = self.db.get_object_by_path(path=self.obj_path)
        self.assertObjectEqual(self.obj, session_obj)

        self.assertRaises(DatabaseException, self.db.create_object, self.obj_path, self.obj_type, self.obj_size)

    def test_get_not_existed_object(self):
        path = '/another/test/path'
        self.assertIsNone(self.db.get_object_by_path(path=path))

    def test_create_cardinality(self):
        self.db.create_cardinality(object=self.obj, nbr_of_elements=5)

        self.assertRaises(DatabaseException, self.db.create_cardinality, self.obj, 5)
