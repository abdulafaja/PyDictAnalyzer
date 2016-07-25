import unittest
from pydictanalyzer.exceptions import FileSystemException
from pydictanalyzer.filesystem import FileSystem


class FileSystemTestCase(unittest.TestCase):
    not_dir_file_path = 'tests/filesystem_tests_dir/test_1_file'
    not_recursive_dir_path = 'tests/filesystem_tests_dir/test_1_dir_3_elements_not_recursive'
    recursive_dir_path = 'tests/filesystem_tests_dir/test_1_dir_5_elements_recursive'

    def assertListLengthEqual(self, filest_list, items):
        self.assertIsInstance(filest_list, list)
        self.assertEqual(len(filest_list), items)

    def test_read_dir(self):
        self.assertRaises(FileSystemException, FileSystem.get_files_list_in_dir_recursive, self.not_dir_file_path)

        files_list = FileSystem.get_files_list_in_dir_recursive(self.not_recursive_dir_path)
        self.assertListLengthEqual(files_list, 3)

        files_list = FileSystem.get_files_list_in_dir_recursive(self.recursive_dir_path)
        self.assertListLengthEqual(files_list, 5)
