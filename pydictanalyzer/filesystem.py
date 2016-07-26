import os

from pydictanalyzer.exceptions import FileSystemException


class FileSystem(object):
    @classmethod
    def get_files_list_in_dir_recursive(cls, dir_path, append_dir_path=True):
        """
        Get the list of files in directory.
        The path should be a directory.
        If the path is not directory function raises FileSystemException

        :param dir_path: Path to the directory
        :type dir_path: str
        :return: List of files in directory
        :rtype: list
        """
        dir_path = cls.create_abs_path(dir_path)
        if not cls.is_dir(dir_path):
            raise FileSystemException("Not a dir path")
        files_list = [] if not append_dir_path else [dir_path]
        for root, dirs, files in os.walk(dir_path):
            files_list += [os.path.join(root, path) for path in dirs + files]
        return files_list

    @classmethod
    def remove_file_if_exists(cls, path):
        """
        Check if given path is a file and remove it

        :param path: Path to check
        :type path: str
        :return: None
        :rtype: None
        """
        path = cls.create_abs_path(path)
        if not cls.file_exists(path):
            return
        if not cls.is_file(path):
            raise FileSystemException("Path is not a file")
        cls.remove_file(path)

    @classmethod
    def create_abs_path(cls, path):
        """
        Change given path to absolute

        :param path: Path to change
        :type path: str
        :return: Absolute path
        :rtype: str
        """
        if not cls.is_abs(path):
            path = os.path.abspath(path)
        return path

    @staticmethod
    def is_dir(path):
        """
        Check if the path is directory

        :param path: File path
        :type path: str
        :return: Boolean value if path is a dir path
        :rtype: bool
        """
        return os.path.isdir(path)

    @staticmethod
    def is_file(path):
        """
        Check if the path is a file

        :param path: File path
        :type path: str
        :return: Boolean value if path is a file path
        :rtype: bool
        """
        return os.path.isfile(path)

    @staticmethod
    def is_symlink(path):
        """
        Check if the path is a symlink

        :param path: File path
        :type path: str
        :return: Boolean value if path is a file path
        :rtype: bool
        """
        return os.path.islink(path)

    @staticmethod
    def is_abs(path):
        """
        Check if the path is an absolute path

        :param path: Path to check
        :type path: str
        :return: Boolean value if path is an absolute
        :rtype: bool
        """
        return os.path.isabs(path)

    @staticmethod
    def file_exists(path):
        """
        Check if given path exists

        :param path: Path to the file
        :type path: str
        :return: Boolean value if given path exists or not
        :rtype: bool
        """
        return os.path.exists(path)

    @staticmethod
    def remove_file(path):
        """
        Remove file from given path

        :param path: Path to remove
        :type path: str
        :return: None
        :rtype: None
        """
        os.remove(path)

    @staticmethod
    def get_size(path):
        """
        Get the given path size

        :param path: Path to get size
        :type path: str
        :return: Number of bytes
        :rtype: int
        """
        return os.path.getsize(path)
