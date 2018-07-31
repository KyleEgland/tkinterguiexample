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
        self.entry_widget_lbl = tk.Label(self, text='Enter information:')
        self.entry_widget_lbl.grid(row=0, column=0, sticky='ns', padx=5,
                                   pady=5)

        self.entry_widget = tk.Entry(self)
        self.entry_widget.grid(row=0, column=1, padx=5, pady=5)

        self.key_bind()

        # Row 1
        # Text box
        self.t_box = tk.Text(self)
        # Insert some "default text" into the text box.  The '1.0' is a spacial
        # reference for where to insert text - 1 is line one and 0 is the 0th
        # character.  Line references start at 1 and character references start
        # at 0.
        self.t_box.insert('1.0', '(Change this text)')
        self.t_box.grid(row=1, columnspan=2, padx=5, pady=5, sticky='ew')

        # ----------------------- #
        # Alternate Tab Functions #
        # ----------------------- #
    def txt_box_update(self, event):
        new_text = self.entry_widget.get()
        self.t_box.insert('1.0', new_text)

    # Bind the Enter key to the entry widget and the txt_box_update func
    def key_bind(self):
        self.entry_widget.bind('<Return>', self.txt_box_update)
