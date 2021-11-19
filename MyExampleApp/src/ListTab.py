#! python3
#
# ListTab.py contains the tkinter Frame object that shares the same name
# (ListTab) which provides an example of the listbox widget within tkinter.
import logging
import tkinter as tk
import tkinter.ttk as ttk


class ListTab(tk.Frame):

    def __init__(self, parent):

        # Instatiating a logger for the object
        self.logger = logging.getLogger("app-logger.TimerTab")
        self.logger.debug("__init__ of ListTab starting...")

        tk.Frame.__init__(self, parent)

        # This tab, having more UI components, has more rows and columns than
        # the TimerTab and TextEditorTab which can add another layer of
        # complexity - keeping all this info straight. Would highly recommend
        # sketching out applications and adding in gridlines to help visuallize
        # what the program is doing (see documentation).
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.rowconfigure(self, 1, weight=1)
        tk.Grid.rowconfigure(self, 2, weight=1)
        tk.Grid.rowconfigure(self, 3, weight=1)
        tk.Grid.rowconfigure(self, 4, weight=1)

        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 1, weight=1)
        tk.Grid.columnconfigure(self, 2, weight=1)
        tk.Grid.columnconfigure(self, 3, weight=1)

        # ------------------------ #
        # ROW 0 - Input Information#
        # ------------------------ #

        self.input_info_label = tk.Label(
            self, text='Input Info'
        )
        self.input_info_label.grid(
            row=0, column=0, sticky='ew', padx=5, pady=5
        )

        self.input_info_entry = tk.Entry(self)
        self.input_info_entry.grid(
            row=0, column=1, sticky='ew', columnspan=2
        )

        self.add_button = ttk.Button(
            self, text="Add", command=self.add_input_info
        )
        self.add_button.grid(
            row=0, column=3,
        )

        # ----------------------------------------_------ #
        # ROW 1 - top of list boxes and move_right_button #
        # -----------------------------------------_----- #
        self.start_listbox = tk.Listbox(self)
        self.start_listbox.grid(
            row=1, column=1, rowspan=3, sticky="nsew", padx=15, pady=15
        )

        self.move_right_button = ttk.Button(
            self, text=">", command=self.move_item_right
        )
        self.move_right_button.grid(
            row=1, column=2
        )

        self.other_listbox = tk.Listbox(self)
        self.other_listbox.grid(
            row=1, column=3, rowspan=3, sticky="nsew", padx=15, pady=15
        )

        # ---------------------------------------------- #
        # Row 2 - middle of listbox and move_left_button #
        # ---------------------------------------------- #
        self.move_left_button = ttk.Button(
            self, text="<", command=self.move_item_left
        )
        self.move_left_button.grid(
            row=2, column=2
        )

        # -------------------------- #
        # Row 3 - bottom of list box #
        # -------------------------- #
        # These comments exist as a reminder of what the program visually looks
        # like, there is no code needed for row 3 (as of this commit).

        # ------------------------------ #
        # Row 4 - List box label widgets #
        # ------------------------------ #
        self.start_listbox_label = tk.Label(
            self, text="Start Listbox"
        )
        self.start_listbox_label.grid(
            row=4, column=1, sticky="nsew", pady=5
        )

        self.other_listbox_label = tk.Label(
            self, text="Other Listbox"
        )
        self.other_listbox_label.grid(
            row=4, column=3, sticky="nsew", pady=5
        )

    def add_input_info(self):
        # add_input_info retrieves the information from the entry widget and
        # "adds it" to the start_listbox widget
        pass

    def move_item_right(self):
        # move_item_right moves an item from the "start_listbox" to the
        # "other_listbox"
        pass

    def move_item_left(self):
        # move_item_left moves an item from the "other_listbox" to the
        # "start_listbox"
        pass
