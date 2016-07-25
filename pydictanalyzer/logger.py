import logging
from logging.config import fileConfig

fileConfig('config/logger.cfg')
PyDictAnalyzerLogger = logging.getLogger()
