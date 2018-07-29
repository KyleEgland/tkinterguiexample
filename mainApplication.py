#! python3
#
# Main program for a GUI with tkinter
# Import information
# tkinter = GUI module, used to construct GUI
# ttk = tkinter styling module, more GUI stuff
# logging = handles logging - see Logger Setup for more information
# os = used here to handle directories - see Logger Setup
# sys = used here to exit application before run - see Logger Setup
import tkinter as tk
import tkinter.ttk as ttk
import logging
import os
import sys
# "Local" imports - files that were created and should be placed in the same
# directory as this file.
from primarytab import PrimaryTab
from alternatetab import AlternateTab
from thirdtab import OtherTab


# ------------ #
# Logger Setup #
# ------------ #
# Check for the existence of a 'logs' folder - should one not exist, create it
if os.path.exists('./logs/'):
    pass
else:
    try:
        os.mkdir('./logs/')
    except Exception as e:
        print('[-] Unable to create directory - please check permissions')
        sys.exit()

# Log levels (low-high): Debug -> Info -> Warning -> Error -> Critical
# Instantiate a logger - instead of using root - to allow files to log
# independently (if there are multiple files in a project)
logger = logging.getLogger(__name__)

# This establishes what level to log (ref. log levels above)
logger.setLevel(logging.DEBUG)

# Format the string that prepends the information that goes into the log file
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s',
                              datefmt='%d-%b-%Y %H')

# Create/name the log file
file_handler = logging.FileHandler('./logs/{}.log'.format(__name__))

# Link the specified format above to the logger
file_handler.setFormatter(formatter)

# Capture only Errors and above in file handler - this overrides ".setLevel"
# for the file
file_handler.setLevel(logging.ERROR)

# Adding stream handler to put debug statements in console
stream_handler = logging.StreamHandler()
# Don't need to set logging level on this because the logger itself is
# set to DEBUG already
# Set formatting of stream handler to be the same as the log file
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
# Add stream handler to the logger
logger.addHandler(stream_handler)
# NOTES:
# use logger.exception() to get the traceback in addtion to log message

# ---------- #
# End Logger #
# ---------- #


class MyApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Give the window an icon (must be in dir desginated)
        # tk.Tk.iconbitmap(self, default='icons/example_icon.ico')
        # Give the window a title (displayed in title bar; top of window)
        tk.Tk.wm_title(self, 'Example GUI')

        # Create the Notebook widget that will comprise the main part
        # of the application
        self.notebook = ttk.Notebook(self)
        # Use pack geometry to fill window with the Notebook widget
        self.notebook.pack(fill='both', expand=True)

        # Instantiate Notebook pages, note that the order here determines load
        # order - this can be important depending on desired effect(s)
        primary_tab = PrimaryTab(self.notebook)
        alt_tab = AlternateTab(self.notebook)
        other_tab = OtherTab(self.notebook)

        # Add the pages to the Notebook; this order determines appearnce on
        # the window - it can be specified explicitely as well
        self.notebook.add(primary_tab, text='Main')
        self.notebook.add(alt_tab, text='Alternate')
        self.notebook.add(other_tab, text='Just Buttons')

        # Top menu bar (e.g. File, Edit, etc.)
        # Menu bar will be visible across all tabs as when it is placed here
        # in the "Main window"
        menu_bar = tk.Menu(self)

        # Creating menus for the menu bar
        # "file_menu" instantiates the variable that is to serve as the actual
        # "File" menu.  Using "tearoff=0" prevents it from being moved -
        # meaning clicked and dragged to somewhere else
        file_menu = tk.Menu(menu_bar, tearoff=0)

        # Creating commands to house inside menus of menu bar
        file_menu.add_command(label='New Thing', accelerator='Ctrl+N')
        file_menu.add_command(label='Load Thing', accelerator='Ctrl+L')
        file_menu.add_command(label='Save Thing', accelerator='Ctrl+S')

        # Adding menus to menu bar
        # Add cascade to allow cascade effect over window.
        # Cascade effect is the "normal" file menu effect
        menu_bar.add_cascade(label='File', underline=0, menu=file_menu)
        # Identify "menu_bar" as the menu for the application
        self.config(menu=menu_bar)


app = MyApp()
app.mainloop()
