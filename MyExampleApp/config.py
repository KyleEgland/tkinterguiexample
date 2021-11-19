#! python
#
# config.py sets up basic information for the application such as logging
# configuration, establishing environment variables, etc. This is "general
# application" level information - needed by most or multiple parts of the app.
import logging
import logging.config
import os


basedir = os.getcwd()


# Logging will be done using the built-in Python logging module and will be
# configured using the dictionary configuration method.
LOGGING = {
    # From the Python 3 documentation:
    # "version - to be set to an integer value representing the schema version.
    # The only valid value at present is 1, but having this key allows the
    # schema to evolve while still preserving backwards compatibility."
    "version": 1,
    # disable_existing_loggers will disable all other loggers if set to True;
    # there's, really, just the "root" logger ("on" by default).
    "disable_existing_loggers": False,
    "formatters": {
        # "default" is the name of the logging formatter created below. This
        # sets up how the output will look and allows the formatting of the
        # date string as well.
        "default": {
            "class": "logging.Formatter",
            "format": "%(asctime)s [ %(filename)s ] Line: %(lineno)s "
            "(%(levelname)s) %(name)s:  %(message)s",
            # Example date format: "%Y-%m-%d %H:%M:%S"
            "datefmt": "%H:%M:%S"
        }
    },
    "handlers": {
        # "default" is the name of the logging handler created below.
        "default": {
            # "class" can be of several types - StreamHandler is for console
            # output, there's also FileHandler, RtotatingFileHandler, amongst
            # others - see Python documentation
            # https://docs.python.org/3/library/logging.handlers.html
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "default"
        }
    },
    "loggers": {
        "app-logger": {
            "handlers": ["default"],
            "level": "DEBUG",
        }
    }
}

logging.config.dictConfig(LOGGING)
logger = logging.getLogger(f"app-logger.{__name__}")
logger.debug("Creation configuration object")


class Config(object):
    # This configuration object is intended to be consumed by the primary
    # application in order to pass information between disparate components.
    def __init__(self, *args):
        # Creating a configuration logger
        self.logger = logging.getLogger("app-logger.Config")
        self.logger.debug("__init__ of Config object starting...")

        self.APP_DIR = basedir

        self.APP_ENV = os.environ.get("APP_ENV") or "development"
        self.logger.debug(f"App_ENV: {self.APP_ENV}")

        self.APP_NAME = os.environ.get("APP_NAME") or "My Example App"
        self.logger.debug(f"APP_NAME: {self.APP_NAME}")

        self.APP_VERSION = os.environ.get("APP_VERSION") or "0.1.1"
        self.logger.debug(f"APP_Version: {self.APP_VERSION}")

        self.APP_ICON = os.path.join(
            basedir, "MyExampleApp/src/icons/favicon.ico"
        )

        self.logger.debug("...Config __init__ complete")
