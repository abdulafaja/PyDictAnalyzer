import os

from pydictanalyzer.exceptions import FileSystemException


class FileSystem(object):
    @classmethod
    def get_files_list_in_dir_recursive(cls, dir_path):
        """
        Get the list of files in directory.
        The path should be a directory.
        If the path is not directory function raises FileSystemException

        :param dir_path: Path to the directory
        :type dir_path: str
        :return: List of files in directory
        :rtype: list
        """
        if not FileSystem._is_abs(dir_path):
            dir_path = os.path.abspath(dir_path)
        if not cls._is_dir(dir_path):
            raise FileSystemException("Not a dir path")
        files_list = []
        for root, dirs, files in os.walk(dir_path):
            dir_files = [os.path.join(root, path) for path in dirs + files]
            files_list += dir_files
        return files_list

    @staticmethod
    def _is_dir(dir_path):
        """
        Check if the path is directory

        :param dir_path: File path
        :type dir_path: str
        :return: Boolean value if path is a dir path
        :rtype: bool
        """
        return os.path.isdir(dir_path)

    @staticmethod
    def _is_abs(path):
        """
        Check if the path is an absolute path

        :param path: Path to check
        :type path: str
        :return: Boolean value if path is an absolute
        :rtype: bool
        """
        return os.path.isabs(path)
