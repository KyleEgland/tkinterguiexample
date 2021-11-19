#! python
#
# __main__.py is called when MyExampleApp is invoked from the command line,
# this file is the "starting point" for the code. The Config object is imported
# from the config.py file so that we may utilize it throughout the program;
# instantiating it here allows us control of app contruction - creating our
# logger before the various components of the application create theirs,
# establishing environment variables, etc.
from config import Config
from src import MyAppWindow


# Instatiating a configuration object via the Config class created in the
# config.py file.
Config = Config()

# Instantiating a new MyAppWindow object in which the new Config object is
# passed.
app = MyAppWindow(Config)

# Starting up the application by invoking the .mainloop() method (provided by
# tkinter when it was subclassed in the "main app" window class).
app.mainloop()
