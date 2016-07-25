class PyAnalyzerException(Exception):
    """
    Base PyAnalyzer exception class
    """
    pass


class FileSystemException(PyAnalyzerException):
    """
    Exception raised by file system class.
    """
    pass
