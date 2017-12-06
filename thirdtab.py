#! python3
#
# Primary tab for mainApplication of example GUI
# Import information:
# tkinter = GUI module, used to construt the GUI
# ttk = tkinter styling, more GUI stuff
import tkinter as tk
import tkinter.ttk as ttk


class OtherTab(tk.Frame):
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

        # Row 0
        # Two buttons
        button_1 = ttk.Button(self, text='Button 1')
        button_1.grid(row=0, column=0, sticky='nsew')
        button_2 = ttk.Button(self, text='Button 2')
        button_2.grid(row=0, column=1, sticky='nsew')

        # Row 1
        # Two more buttons
        button_3 = ttk.Button(self, text='Button 3')
        button_3.grid(row=1, column=0, sticky='nsew')
        button_4 = ttk.Button(self, text='Button 4')
        button_4.grid(row=1, column=1, sticky='nsew')
