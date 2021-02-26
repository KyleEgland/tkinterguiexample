import tkinter as tk
import tkinter.ttk as ttk
from MyExampleApp.PrimaryTab import PrimaryTab
from MyExampleApp.SecondaryTab import SecondaryTab
from MyExampleApp.TextEditorTab import TextEditorTab
from MyExampleApp.ButtonsTab import ButtonsTab

class MyAppWindow(tk.Tk):
    # MyApp is the class that represents the entire TKinter applications - it
    # contains all components of the GUI application

    def __init__(self, Config, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
    
        # Application configuration information
        self.Config = Config()
    
        # Give the window an icon (must be in dir desginated)
        tk.Tk.iconbitmap(self, default=self.Config.APP_ICON)
        # Give the window a title (displayed in title bar; top of window)
        tk.Tk.wm_title(self, self.Config.APP_NAME)

        # Create the Notebook widget that will contain the bulk of the app -
        # all of the tabs
        self.notebook = ttk.Notebook(self)

        # Use pack geometry to fill window with the Notebook widget. Using pack
        # instead of grid because it should simply fill the whole space.
        self.notebook.pack(fill='both', expand=True)

        # Instantiate Notebook pages, note that the order here determines load
        # order - this can be important depending on desired effect(s)
        primary_tab = PrimaryTab(self.notebook)
        secondary_tab = SecondaryTab(self.notebook)
        text_tab = TextEditorTab(self.notebook)
        buttons_tab = ButtonsTab(self.notebook)

        # Add the pages to the Notebook; this order determines appearnce on
        # the window - it can be specified explicitely as well
        self.notebook.add(primary_tab, text='Primary Tab')
        self.notebook.add(secondary_tab, text='Secondary Tab')
        self.notebook.add(text_tab, text='Text Editor')
        self.notebook.add(buttons_tab, text='Just Buttons')

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
