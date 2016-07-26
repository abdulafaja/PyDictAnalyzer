import sys

from pydictanalyzer.argument_parser import ArgumentParser
from pydictanalyzer.database import Database
from pydictanalyzer.exceptions import PyDictAnalyzerException
from pydictanalyzer.filesmanager import FilesManager
from pydictanalyzer.filesystem import FileSystem


def prepare_database(database_name):
    database_path = FileSystem.create_abs_path(database_name)
    FileSystem.remove_file_if_exists(database_path)
    connection_string = Database.get_connection_string(database_path)
    return Database(connection_string)


def load_files(directory_name):
    files_manager = FilesManager()
    files_manager.load_files(directory_name)
    return files_manager


def main():
    arg_parser = ArgumentParser()
    database = prepare_database(arg_parser.database_name)
    files_manager = load_files(arg_parser.dir_name)
    files_manager.save_files(database)


if __name__ == "__main__":
    try:
        main()
    except PyDictAnalyzerException as e:
        print(e)
        sys.exit(1)
