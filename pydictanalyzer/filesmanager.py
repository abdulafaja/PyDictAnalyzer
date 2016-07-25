import os

from pydictanalyzer.filesystem import FileSystem
from pydictanalyzer.objects import Directory, File, Other


class FilesManager(object):
    """
    Class to load files from given path and store it into database
    """
    def __init__(self):
        self._files = []

    @property
    def files(self):
        return self._files

    def load_files(self, dir_path):
        """
        Load files from given directory, create its virtual representation and add to object's files list

        :param dir_path: Path to the directory from files should be loaded
        :type dir_path: str
        :return: None
        :rtype: None
        """
        for path in FileSystem.get_files_list_in_dir_recursive(dir_path):
            if not os.path.islink(path) and os.path.isfile(path):
                file = File(path)
            elif not os.path.islink(path) and os.path.isdir(path):
                file = Directory(path)
            else:
                file = Other(path)
            self._files.append(file)

    def save_files(self, database):
        """
        Store loaded files into database

        :param database: Database class instance
        :type database: pydictanalyzed.database.Database
        :return: None
        :rtype: None
        """
        for file in self.files:
            file.add_to_db(database)
