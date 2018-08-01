#! python
#
# Alternate tab for Example GUI program.
# This tab contains an entry and text box widget.
# Import information:
# tkinter = GUI module, used to construct the GUI
# ttk = tkinter styling, more GUI stuff
import tkinter as tk
import tkinter.ttk as ttk
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

        # bind the enter key to the entry widget
        self.key_bind()

        # Row 1
        # Text box
        self.t_box = tk.Text(self, width=40, height=12)
        # Insert some "default text" into the text box.  The '1.0' is a spacial
        # reference for where to insert text - 1 is line one and 0 is the 0th
        # character.  Line references start at 1 and character references start
        # at 0.
        self.t_box.insert('1.0', '(Change this text)')
        self.t_box.grid(row=1, columnspan=2, padx=5, pady=5, sticky='ew')
        # Instantiate a scoll bar to interact with the text box - they are
        # separate widgets themselves
        self.txt_scroll = ttk.Scrollbar(self, orient='vertical',
                                        command=self.t_box.yview)
        # Place the scroll bar within the window
        self.txt_scroll.grid(column=1, row=1, sticky='nse')
        # Configure the text box so that the text box can interact with the
        # scoll bar
        self.t_box.configure(yscrollcommand=self.txt_scroll.set)

        # ----------------------- #
        # Alternate Tab Functions #
        # ----------------------- #
    def txt_box_update(self, event):
        # Get the contents of the entry widget and add a new line to the end of
        # it.  This will push down the previous text and put the entry widget
        # contents on top of it.
        new_text = self.entry_widget.get() + "\n"
        # Insert the newly created string into the text box
        self.t_box.insert('1.0', new_text)
        # Delete what was in the entry widget
        self.entry_widget.delete(0, 'end')

    # Bind the Enter key to the entry widget and the txt_box_update func
    def key_bind(self):
        self.entry_widget.bind('<Return>', self.txt_box_update)
