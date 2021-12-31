#! python3
#
# __init__.py
# This is the application's initialization - where application startup begins.
# The main application is collected and started here - the window that contains
# everthing is instantiated and the tabs are imported and consumed.
import logging
from tkinter import messagebox as mb
import tkinter as tk
import tkinter.ttk as ttk
from src.TimerTab import TimerTab
from src.ListTab import ListTab
from src.TextEditorTab import TextEditorTab


class MyAppWindow(tk.Tk):
    # MyAppWindow is a class that represents the entire TKinter applications;
    # it contains all components of the GUI application (e.g., tabs, menus,
    # etc.).

    def __init__(self, Config, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        # Creating a logger for the "main window" by sub-classing the logger
        # created by the config.py file
        self.logger = logging.getLogger("app-logger.MyAppWindow")
        self.logger.debug("__init__ of MyAppWindow object starting...")

        # self.Config is being set to the configuration object (Config)
        self.Config = Config

        # Give the window an icon. This value is set by the APP_ICON attribute
        # of the Config class that was passed into the MyAppWindow upon
        # instantiation.
        # TODO: Fix app icon - there is an issue with nix systems (cannot use
        # the .ico file)
        # self.logger.debug(f"Iconbitmap: {self.Config.APP_ICON}")
        # tk.Tk.iconbitmap(self, default=self.Config.APP_ICON)

        # Give the window a title; the string value will be displayed in title
        # bar (at the top of window).
        tk.Tk.wm_title(self, self.Config.APP_NAME)

        # Create the Notebook widget that will contain the bulk of the app -
        # all of the tabs
        self.notebook = ttk.Notebook(self)

        # Use pack geometry to fill window with the Notebook widget. Using pack
        # instead of grid because it should simply fill the whole space.
        self.notebook.pack(fill='both', expand=True)

        # Instantiate Notebook pages, note that the order here determines load
        # order - this can be important depending on desired effect(s)
        self.timer_tab = TimerTab(self.notebook)
        self.list_tab = ListTab(self.notebook)
        self.text_tab = TextEditorTab(self.notebook)

        # Add the pages to the Notebook; this order determines appearnce on
        # the window - it can be specified explicitely as well
        self.notebook.add(self.timer_tab, text='Timer')
        self.notebook.add(self.list_tab, text='Lists')
        self.notebook.add(self.text_tab, text='Text Editor')

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
        file_menu.add_command(
            label='New Thing', accelerator='Ctrl+N', command=self.new_thing
        )
        file_menu.add_command(
            label='Load Thing', accelerator='Ctrl+L', command=self.load_thing
        )
        file_menu.add_command(
            label='Save Thing', accelerator='Ctrl+S', command=self.save_thing
        )

        # Adding menus to menu bar
        # Add cascade to allow cascade effect over window.
        # Cascade effect is the "normal" file menu effect
        menu_bar.add_cascade(label='File', underline=0, menu=file_menu)
        # Identify "menu_bar" as the menu for the application
        self.config(menu=menu_bar)

        # Binding menu key combinations - invokings a method in this manner
        # will pass the function an event. This event is not needed in this
        # instance so the "lambda event=None" calls the function without
        # passing in the event.
        self.bind("<Control-n>", lambda event=None: self.new_thing())
        self.bind("<Control-l>", lambda event=None: self.load_thing())
        self.bind("<Control-s>", lambda event=None: self.save_thing())

        self.logger.debug("...MyAppWindow __init__ complete")

    def new_thing(self):
        mb.showinfo(
            title="New Thing",
            message="This menu has been descoped from the project"
        )

    def load_thing(self):
        mb.showinfo(
            title="Load Thing",
            message="This example should add some level of clarity on how the"
            "\"file\" menu could work."
        )

    def save_thing(self):
        mb.showinfo(
            title="Save Thing",
            message="Just another message box :)"
        )
