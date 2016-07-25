class PyDictAnalyzerException(Exception):
    """
    Base PyAnalyzer exception class
    """
    pass


class DatabaseException(PyDictAnalyzerException):
    """
    Database exception
    """
    pass


class FileSystemException(PyDictAnalyzerException):
    """
    Exception raised by file system class.
    """
    pass
