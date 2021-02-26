#! python3
#
# tkinterguiexample
# MyExampleApp
# __init__.py
# This is the application's init - where application startup begins. TKinter
# app setup continues in the mainwindow file where the application class is
# created and imported here to create the application window.
import logging
import os
import sys
# Local imports
from MyExampleApp.mainwindow import MyApp
from config import Config


def create_app(config_class=Config):
    # Borrowing from the Flask design idea of the application factory; this
    # function returns an application which will be invoked by the caller

    app = MyApp(config_class)

    return app
