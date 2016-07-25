import hashlib
import os

from pydictanalyzer.filesystem import FileSystem


class Object(object):
    """
    Main class to manage objects.
    """
    def __init__(self, path):
        self._path = path

    @property
    def type(self):
        raise NotImplementedError

    @property
    def size(self):
        return os.stat(self.path).st_size

    @property
    def path(self):
        return self._path

    def add_to_db(self, database):
        return database.create_object(self.path, self.type, self.size)


class Directory(Object):
    """
    Dictionary representation
    """
    @property
    def type(self):
        return 'd'

    @property
    def nbr_of_elements(self):
        return len(FileSystem.get_files_list_in_dir_recursive(self.path, append_dir_path=False))

    def add_to_db(self, database):
        object = super(Directory, self).add_to_db(database)
        database.create_cardinality(object, self.nbr_of_elements)


class File(Object):
    """
    File representation
    """
    @property
    def type(self):
        return 'f'

    @property
    def checksum(self):
        return hashlib.md5(open(self.path, 'rb').read()).hexdigest()

    def add_to_db(self, database):
        object = super(File, self).add_to_db(database)
        database.create_checksum(object, self.checksum)


class Other(Object):
    """
    Not dictionary nor file object
    """
    @property
    def type(self):
        return 'o'
