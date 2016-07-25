import os
import unittest

from pydictanalyzer.database import Database
from pydictanalyzer.exceptions import FileSystemException
from pydictanalyzer.filesmanager import FilesManager


class FilesManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.db = Database('sqlite://')
        self.fm = FilesManager()
        self.objects_tests_dir_path = 'tests/objects_tests_dir'

    def assertOtherObjectInDB(self, path):
        object = self.db.get_object_by_path(path)
        self.assertIsNotNone(object)

    def assertFileObjectInDB(self, path):
        object = self.db.get_object_by_path(path)
        self.assertIsNotNone(object)
        checksum = self.db.get_checksum(object)
        self.assertIsNotNone(checksum)

    def assertDirectoryObjectInDB(self, path):
        object = self.db.get_object_by_path(path)
        self.assertIsNotNone(object)
        cardinality = self.db.get_cardinality(object)
        self.assertIsNotNone(cardinality)

    def test_load_files_existed_path(self):
        self.fm.load_files(self.objects_tests_dir_path)

        self.assertEqual(len(self.fm.files), 5)

    def test_load_files_not_existed_path(self):
        self.assertRaises(FileSystemException, self.fm.load_files, 'not/existed/path')

    def test_save_file_into_database(self):
        self.fm.load_files(self.objects_tests_dir_path)

        self.fm.save_files(self.db)

        for file in self.fm.files:
            if not os.path.islink(file.path) and os.path.isfile(file.path):
                self.assertFileObjectInDB(file.path)
            elif not os.path.islink(file.path) and os.path.isdir(file.path):
                self.assertDirectoryObjectInDB(file.path)
            else:
                self.assertOtherObjectInDB(file.path)
