#! python
#
# TextEditorTab.py
import tkinter as tk
import tkinter.ttk as ttk


class TextEditorTab(tk.Frame):

    def __init__(self, parent):

        tk.Frame.__init__(self, parent)

        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.rowconfigure(self, 1, weight=10)

        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 1, weight=2)
        tk.Grid.columnconfigure(self, 2, weight=1)
        tk.Grid.columnconfigure(self, 3, weight=1)

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
            self, text="N/A"
        )
        self.loaded_file_name_label.grid(
            row=0, column=1, sticky="nsew", padx=5, pady=5
        )

        self.open_button = ttk.Button(
            self, text="Open"
        )
        self.open_button.grid(
            row=0, column=2, sticky="ew", padx=5, pady=5
        )

        self.save_button = ttk.Button(
            self, text="Save"
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
