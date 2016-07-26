import argparse


class ArgumentParser(object):
    def __init__(self):
        parser = argparse.ArgumentParser(description='Analyze directory. Store content\'s data in sqlite db.')
        parser.add_argument('nazwa_katalogu', nargs=1, help='Directory to analyze.')
        parser.add_argument('nazwa_bazy', nargs=1, help='A name of the database.')

        self._args = parser.parse_args()

    @property
    def dir_name(self):
        return self._args.nazwa_katalogu[0]

    @property
    def database_name(self):
        return self._args.nazwa_bazy[0]
