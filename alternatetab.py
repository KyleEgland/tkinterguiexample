#! python
#
# Alternate tab for Example GUI program
# Import information:
# tkinter = GUI module, used to construct the GUI
# ttk = tkinter styling, more GUI stuff
import tkinter as tk
# import tkinter.ttk as ttk


class AlternateTab(tk.Frame):
    # Initilization function
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        # The "rowconfigure" and "columnconfigure" tell the program
        # how to resize widgets when the window is resized
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.rowconfigure(self, 1, weight=1)

        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 1, weight=1)

        # Row 0
        # Entry
        entry_widget_lbl = tk.Label(self, text='Enter information:')
        entry_widget_lbl.grid(row=0, column=0, sticky='ns', padx=5, pady=5)

        entry_widget = tk.Entry(self)
        entry_widget.grid(row=0, column=1, padx=5, pady=5)

        # Row 1
        # Listbox
        a_box = tk.Listbox(self)
        a_box.grid(row=1, columnspan=2, padx=5, pady=5, sticky='ew')
