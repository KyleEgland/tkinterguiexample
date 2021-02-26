#! python
#
# tkinterguiexample
# config.py
# This file sets up basic information for the application such as logging
# setup, establishing environment variables, etc. This is "general application"
# level information - needed by most or multiple parts of the app.
import logging
import os


LOGGING = {
    # This is always 1, see Python's logging documentation for "why"
    "version": 1,
    # disable_existing_loggers does exactly that if set to True. While this
    # would disable the root logger, setting this value to False seems to
    # cause more problems than it solves.
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": "%(asctime)s %(name)s %(levelname)s: %(message)s"
        }
    },
    "hanlders": {
        "console": {
            "level": os.environ.get("CONSOLE_LOG_LEVEL") or "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "console"
        }
    },
    "loggers": {
        "App": {
            "handlers": ["console"],
            "level": os.environ.get("APP_LOG_LEVEL") or "DEBUG"
        }
    }
}


class Config(object):
    def __init__(self, *args):
        self.APP_ENV = os.environ.get("APP_ENV") or "development"
        self.APP_NAME = os.environ.get("APP_NAME") or "My Example App"
        self.APP_VERSION = os.environ.get("APP_VERSION") or "2.0.0"
