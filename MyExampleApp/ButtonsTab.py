#! python3
#
# Primary tab for mainApplication of example GUI
# Import information:
# tkinter = GUI module, used to construt the GUI
# ttk = tkinter styling, more GUI stuff
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mb


class ButtonsTab(tk.Frame):
    # Initialization function
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        # The "rowconfigure" and "columnconfigure" tell the program
        # how to resize widgets when the window is resized
        # Weight affects how the item will be scaled in relation
        # to the other elements that are bing re-sized
        # E.g. a row with weight 2 will scale more than a row with weight 1
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.rowconfigure(self, 1, weight=1)

        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 1, weight=1)

        # ------------------- #
        # Row 0 - Two buttons #
        # ------------------- #
        # The first button will create a 'showinfo' message window when
        # clicked.  The 'command' option is used to specify the function
        button_1 = ttk.Button(self, text='Alert\nText Box',
                              command=self.info_box)
        button_1.grid(row=0, column=0, sticky='nsew')
        # The second button will create an 'askyesno' message window, which,
        # will return yes or no to the caller.  However, the return function is
        # not utilized.
        button_2 = ttk.Button(self, text='Yes or No',
                              command=self.check_y_or_n)
        button_2.grid(row=0, column=1, sticky='nsew')

        # ------------------------ #
        # ROW 1 - Two more buttons #
        # ------------------------ #
        # The third betton will create a 'yesnocancel' message window
        button_3 = ttk.Button(self, text='Yes, No, Cancel',
                              command=self.y_n_cancel)
        button_3.grid(row=1, column=0, sticky='nsew')
        # The fourth button will create a 'abortretryignore' message window
        button_4 = ttk.Button(self, text='Abort, Retry, Ignore',
                              command=self.abort_retry_ignore)
        button_4.grid(row=1, column=1, sticky='nsew')

    # ------------- #
    # Class Methods #
    # ------------- #
    # Message box methods:
    #   messagebox.showinfo
    #   messagebox.askyesno
    #   messagebox.askretrycancel
    # Message box types:
    #   ok - default type
    #   okcancel
    #   yesno
    #   yesnocancel
    #   retrycancel
    #   abortretryignore
    def info_box(self):
        mb.showinfo(message='This is built in to TKinter!', icon='info',
                    title='Pop-up', detail='This is a detail message')

    def check_y_or_n(self):
        mb.askyesno(message='Are you learning yet?', icon='question',
                    title='Well?')

    def y_n_cancel(self):
        mb.showerror(message='Is this fun?', icon='warning', title='Another \
Pop-up', detail='Something goes here', type='yesnocancel')

    def abort_retry_ignore(self):
        mb.showwarning(message='What do you want to do here?', icon='warning',
                       title='Last Window', type='abortretryignore')
