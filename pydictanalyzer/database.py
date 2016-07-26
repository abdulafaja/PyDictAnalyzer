from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError, NoSuchModuleError, OperationalError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import FlushError

from pydictanalyzer.exceptions import DatabaseException
from pydictanalyzer.logger import PyDictAnalyzerLogger
from pydictanalyzer.models import Base, Cardinality, Checksum, Object


class Database(object):
    """
    Database class. It store database engine and session
    """
    def __init__(self, connection_string):
        try:
            self._engine = create_engine(connection_string)
            Base.metadata.create_all(self._engine)
        except (OperationalError, NoSuchModuleError) as e:
            PyDictAnalyzerLogger.exception(e)
            raise DatabaseException(e)
        self._session = sessionmaker(bind=self._engine)()

    def _commit(self):
        try:
            self._session.commit()
        except (FlushError, IntegrityError) as e:
            PyDictAnalyzerLogger.exception(e)
            raise DatabaseException(e)

    def create_object(self, path, type, size):
        obj = Object(path=path, type=type, size=size)
        self._session.add(obj)
        return obj

    def get_object_by_path(self, path):
        return self._session.query(Object).filter_by(path=path).first()

    def create_cardinality(self, object, nbr_of_elements):
        cardinality = Cardinality(id=object.id, nbr_of_elements=nbr_of_elements)
        self._session.add(cardinality)
        return cardinality

    def get_cardinality(self, object):
        return self._session.query(Cardinality).get(object.id)

    def create_checksum(self, object, checksum):
        checksum = Checksum(id=object.id, checksum=checksum)
        self._session.add(checksum)
        return checksum

    def get_checksum(self, object):
        return self._session.query(Checksum).get(object.id)

    def apply_changes(self):
        self._commit()

    @staticmethod
    def get_connection_string(database_name):
        return "sqlite:///{}".format(database_name)
