#! python3
#
# TimerTab.py is an example tkinter notebook widget which contains some basic
# "count down timer" function
import logging
from tkinter import messagebox as mb
import tkinter as tk
from tkinter.constants import END
import tkinter.ttk as ttk


class TimerTab(tk.Frame):
    # Initialization function
    def __init__(self, parent):
        #  Instantiate logger
        self.logger = logging.getLogger("app-logger.TimerTab")
        self.logger.debug("__init__ of TimerTab starting...")

        # Initializing the frame, the parent passed in here is the notebook
        # instatiated in the init file and passed when this tab is instatiated
        tk.Frame.__init__(self, parent)

        # ------------- #
        # Tab variables #
        # ------------- #
        # Creating a variable for the number of seconds that is the timer
        self.timer_value = tk.IntVar()
        # Setting its initial value 0
        self.timer_value.set(0)
        # Creating a variable for the timer display
        self.timer_display_value = tk.StringVar()
        # Setting its initial value to 00:00
        self.timer_display_value.set("00:00")

        # ------------------------ #
        # Tab Layout Configuration #
        # ------------------------ #
        # rowconfigure instantiates and establishes some basic attributes
        # of the frame's layout . Weight affects how the item will be scaled in
        # relation to the other elements that are bing re-sized. E.g. a row
        # with weight 1 will scale more than a row with weight 2.
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.rowconfigure(self, 1, weight=1)
        tk.Grid.rowconfigure(self, 2, weight=1)

        # columnconfigure is used to instantiate set the initial attributes of
        # the desired columns
        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 1, weight=1)
        tk.Grid.columnconfigure(self, 2, weight=1)

        # ------------------- #
        # ROW 0 - Timer Label #
        # ------------------- #
        #
        # self.timer_label is the tkinter GUI representation of the count-down
        # timer. This widget will be updated when the user updates the timer
        # (via "set") and when the timer is "in use" (counting down).
        self.timer_label = tk.Label(
            self, textvariable=self.timer_display_value
        )
        # Labels are static text, they don't update unless you force them to do
        # so.
        #
        # Grid is a geometry method that allows for the dictation of a widget's
        # location, size (to a certain extent), and alignment.  Below, the row
        # and column number (everything begins with 0) are specified to dictate
        # where this widget should exist.  After that, the "sticky" alignment
        # is dictated; sticky will stretch widgets like buttons but center
        # widgets like labels.  In this case, 'sne' will align the text between
        # the top and bottom of the cell (sn = south north) and keep the text
        # to the far right of the cell (e = east).
        # self.timer_label.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        self.timer_label.grid(row=0, column=0, sticky='ew', columnspan=2)

        self.timer_start_button = ttk.Button(
            self, text="Start", command=self.start_timer
        )
        self.timer_start_button.grid(
            row=0, column=3, sticky="ew"
        )

        # ------------------- #
        # ROW 1 - Timer input #
        # ------------------- #
        # This section of the tab contains the input widets
        #
        self.timer_input_label = tk.Label(self, text="Input Time")
        self.timer_input_label.grid(row=1, column=0, sticky="ewns")

        self.timer_input_entry = tk.Entry(self)
        self.timer_input_entry.grid(row=1, column=1, sticky="ew")

        self.timer_input_button = ttk.Button(
            self, text='Set', command=self.set_timer
        )
        self.timer_input_button.grid(row=1, column=2)

        # ----------------------- #
        # Row 2 - Input help text #
        # ----------------------- #
        # This section of the tab contains a simple label that instructs the
        # user on how to format value entered into the entry widget above.
        self.input_help_label = tk.Label(
            self,
            text="Enter a timer value as a whole number of seconds, e.g., 120 "
            "(2 min)."
        )
        self.input_help_label.grid(
            row=2, column=0, columnspan=3, sticky="nesw"
        )

        self.logger.debug("...TimerTab __init__ complete")

    # ------------------- #
    # Timer Tab Functions #
    # ------------------- #
    # All functions within the class must reference "self" as the first arg
    def set_timer(self):
        # set_timer is the function "behind" the "Set" button - it is used to
        # initially set the timer
        try:
            timer_get = int(self.timer_input_entry.get())
        except Exception as e:
            # Using a catch-all exception - not a best practice
            self.logger.warning(f"Input exception: {e}")
            mb.showwarning(
                title="Invalid Input Time",
                message="Please enter the number of seconds to be used for the"
                " timer value as a whole number, e.g., 1234"
            )
            # Clear the contents of the entry widget
            self.timer_input_entry.delete(0, END)
            # End the function by returning
            return

        if type(timer_get) is not int:
            # Present a pop-up that indicates an error was made within entry
            mb.showwarning(
                title="Invalid Input Time",
                message="Please enter the number of seconds to be used for the"
                " timer value as a whole number, e.g., 1234"
            )
            # Clear the contents of the entry widget
            self.timer_input_entry.delete(0, END)
            # End the function by returning
            return
        # Set the timer text variable value to the value from the widget
        mins, secs = divmod(timer_get, 60)
        self.timer_display_value.set("{:02d}:{:02d}".format(mins, secs))
        # Set the timer value
        self.timer_value.set(timer_get)
        # Empty the entry widget
        self.timer_input_entry.delete(0, END)
        return

    def start_timer(self):
        # start_timer is the function "behind the start button" which starts
        # the countdown timer.
        # First, get the value of the timer
        timer = self.timer_value.get()
        self.logger.debug(f"start_timer called, timer value: {timer}")

        if timer == 0:
            # Should timer already be 0 then the function is exited
            self.logger.info(
                f"start_timer concluded, timer: {timer}"
            )
            return

        # Decrement timer var
        timer -= 1
        self.timer_value.set(timer)

        # Calculate the remaining time left
        mins, secs = divmod(timer, 60)
        self.logger.debug(
            "start_timer remaining time {:02d}:{:02d}".format(mins, secs)
        )

        self.timer_display_value.set("{:02d}:{:02d}".format(mins, secs))
        self.after(1000, self.start_timer)
