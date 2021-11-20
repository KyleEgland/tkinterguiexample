#! python
#
# TextEditorTab.py
import logging
from tkinter import filedialog as fd
import tkinter as tk
from tkinter.constants import END
import tkinter.ttk as ttk


class TextEditorTab(tk.Frame):

    def __init__(self, parent):
        #  Instantiate logger
        self.logger = logging.getLogger("app-logger.TextEditorTab")
        self.logger.debug("__init__ of TextEditorTab starting...")

        tk.Frame.__init__(self, parent)

        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.rowconfigure(self, 1, weight=10)

        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 1, weight=2)
        tk.Grid.columnconfigure(self, 2, weight=1)
        tk.Grid.columnconfigure(self, 3, weight=1)

        # ------------- #
        # Tab variables #
        # ------------- #
        self.loaded_file_variable = tk.StringVar(
            value="N/A"
        )

        # -------------------------------------- #
        # Row 0 - File label and control buttons #
        # -------------------------------------- #
        self.loaded_file_label = tk.Label(
            self, text="Loaded File:"
        )
        self.loaded_file_label.grid(
            row=0, column=0, sticky="nsew", padx=5, pady=5
        )

        self.loaded_file_name_label = tk.Label(
            self, textvariable=self.loaded_file_variable
        )
        self.loaded_file_name_label.grid(
            row=0, column=1, sticky="nsew", padx=5, pady=5
        )

        self.open_button = ttk.Button(
            self, text="Open", command=self.open_button
        )
        self.open_button.grid(
            row=0, column=2, sticky="ew", padx=5, pady=5
        )

        self.save_button = ttk.Button(
            self, text="Save", command=self.save_button
        )
        self.save_button.grid(
            row=0, column=3, sticky="ew", padx=5, pady=5
        )

        # ---------------------- #
        # Row 1 - Text entry box #
        # ---------------------- #
        self.text_edit = tk.Text(
            self
        )
        # Creating scrollbars for text entry
        self.text_y_scroll = ttk.Scrollbar(
            self, orient="vertical", command=self.text_edit.yview
        )
        self.text_edit["yscrollcommand"] = self.text_y_scroll.set
        self.text_edit.grid(
            row=1, column=0, columnspan=4, sticky="nsew", padx=5, pady=5
        )

        self.logger.debug("...TextEditorTab __init__ complete")

    def open_button(self):
        # open_button will open a file dialog and load the selected text file
        # into the text widget
        filetypes = [
            ("text files", "*.txt")
        ]

        # Calling the filedialog askopenfile method - if a file is chosen, a
        # file object will be returned, otherwise, it is None
        filename = fd.askopenfile(
            title="Load Text File", initialdir="~/",
            filetypes=(filetypes)
        )

        try:
            # Using try to check whether a file was loaded...
            text = filename.read()
        except AttributeError:
            # ...if no file was chosen, an AttributeError will occur on the
            # above operation because None Type object does not have a read()
            # method.
            self.logger.info("open_button - no file chosen")
            return

        # Empty the contents of the text box
        self.text_edit.delete("1.0", END)
        # Insert the contents of the loaded file
        self.text_edit.insert("1.0", text)
        # Set the name of the loaded file to the variable so that the widget
        # displays the loaded file's name
        self.loaded_file_variable.set(filename.name)

        self.logger.info(f"Loaded {filename.name}")

    def save_button(self):
        # save_button simply writes the contents of the text box to the file
        # name that is displayed in the label.
        location = self.loaded_file_variable.get()
        if location == "N/A":
            self.logger.warning("Attempted to save nothing")
            return
        save_file = open(location, 'w')
        save_file.write(self.text_edit.get("1.0", END))
        save_file.close()
        self.logger.info(f"Saved {location}")
