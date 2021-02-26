#! python
#
# tkinterguiexample
# config.py
# This file sets up basic information for the application such as logging
# setup, establishing environment variables, etc. This is "general application"
# level information - needed by most or multiple parts of the app.
import logging
import logging.config
import os


basedir = os.getcwd()


# Logging will be done using the built-in Python logging module and will be
# configured using the dictionary configuration method. The dictionary below
# (LOGGING) also utilizes environment variables in order to lesson the
# requirement for its continuous modification - use the environment file to
# dictate log levels or everything defaults to "development"/"DEBUG"
LOGGING = {
    # version is always one, see Python logging documentation for details
    "version": 1,
    # disable_existing_loggers will disable all other loggers if set to True;
    # note
    "disable_existing_loggers": False,
    "formatters": {
        # dev is the development log formatter
        "default": {
            "class": "logging.Formatter",
            "format": "%(asctime)s [ %(filename)s ] Line: %(lineno)s "
            "(%(levelname)s) %(name)s:  %(message)s",
            "datefmt": "%H:%M:%S"
        }
    },
    "handlers": {
        # dev is the handler used during development as it uses the most
        #     verbose output
        "default": {
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
logger = logging.getLogger("app-logger.settings")
logger.debug("Settings is running...")


class Config(object):
    def __init__(self, *args):
        self.APP_ENV = os.environ.get("APP_ENV") or "development"
        self.APP_NAME = os.environ.get("APP_NAME") or "My Example App"
        self.APP_VERSION = os.environ.get("APP_VERSION") or "2.0.0"
        self.APP_ICON = os.path.join(basedir, "icons/favicon.ico")
