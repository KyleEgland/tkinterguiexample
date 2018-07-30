#! python3
#
# This file handles popups by allowing their creation and providing some
# options for output (I.e. providing a "yes"/"no" selection)
import tkinter as tk
import tkinter.ttk as ttk
# sys is imported for the tests at the bottom; if tests are eliminated from the
# program, the "import sys" line can subsequently be eliminated
import sys


class MessageBox(object):

    def __init__(self, msg, b1, b2, frame, t, entry, dropbox, elements,
                 win_title):

        # Instantiate a "root" window for the class
        root = self.root = tk.Tk()

        # Give the window a title - est. by init
        root.title(win_title)

        # Message to be displayed
        self.msg = str(msg)

        # <Ctrl + C> to copy self.msg
        root.bind('<Control-c>', func=self.to_clip)

        # remove the outer frame if frame=False
        if not frame:
            root.overrideredirect(True)

        # Default return values for the buttons
        self.b1_return = True
        self.b2_return = False

        # if b1 or b2 is a tuple unpack into the button text & return value
        if isinstance(b1, tuple):
            b1, self.b1_return = b1
        if isinstance(b2, tuple):
            b2, self.b2_return = b2

        # Main frame
        frm_1 = tk.Frame(root)
        # Geometry for the frame
        frm_1.pack(ipadx=2, ipady=2)

        # The message
        message = tk.Label(frm_1, text=self.msg)
        message.pack(padx=8, pady=8)

        # If entry=True (I.e. an entry widget was asked for when called) create
        # and set focus to that entry widget
        if entry:
            self.entry = tk.Entry(frm_1)
            self.entry.pack()
            self.entry.focus_set()

        # If dropbox=True (I.e. an entry widget was asked for when called)
        # create the widget and set focus to the dropbox
        if dropbox:
            self.drpbx = ttk.Combobox(frm_1, state='readonly')
            self.drpbx['values'] = elements
            self.drpbx.pack()
            self.drpbx.focus_set()

        # Button frame
        frm_2 = tk.Frame(frm_1)
        frm_2.pack(padx=4, pady=4)

        # Buttons
        if b2:
            btn_1 = ttk.Button(frm_2, width=8, text=b1)
            btn_1['command'] = self.b1_action
            btn_1.pack(side='left')

            btn_2 = ttk.Button(frm_2, width=8, text=b2)
            btn_2['command'] = self.b2_action
            btn_2.pack(side='left')
        else:
            btn_1 = ttk.Button(frm_2, width=8, text=b1)
            btn_1['command'] = self.b1_action
            btn_1.pack()

        if not entry:
            btn_1.focus_set()

        # The enter button will trigger the focused button's action
        btn_1.bind('<KeyPress-Return>', func=self.b1_action)
        if b2:
            btn_2.bind('<KeyPress-Return>', func=self.b2_action)

        # Roughly center the box on screen for accuracy see:
        # http://stackoverflow.com/a/10018670/1217270
        root.update_idletasks()
        xp = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
        yp = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
        geom = (root.winfo_width(), root.winfo_height(), xp, yp)
        root.geometry('{0}x{1}+{2}+{3}'.format(*geom))

        # Call self.close_mod when the close button is pressed
        root.protocol("WM_DELETE_WINDOW", self.close_mod)
        # A trick to activate the window (on windows 7)
        root.deiconify()
        # If 't' is specified, call time_out after 't' seconds
        if t:
            root.after(int(t * 1000), func=self.time_out)

    # Button 1 action function
    def b1_action(self, event=None):
        # First, check to see if there is an entry widget
        try:
            self.returning = self.entry.get()
            self.root.quit()
        except AttributeError:
            # If there is no entry widget, check for a dropbox widget
            try:
                self.returning = self.drpbx.get()
                self.root.quit()
            except AttributeError:
                self.returning = self.b1_return
                self.root.quit()

    def b2_action(self, event=None):
        self.returning = self.b2_return
        self.root.quit()

    # This function (using pass) prevents the "x" from closing the window.
    # Should the window's "x" need to function normally, simply remove "pass"
    # and input whatever code is appropriate.
    def close_mod(self):
        pass
        # self.returning = False
        # self.root.quit()

    def time_out(self):
        try:
            x = self.entry.get()
        except AttributeError:
            self.returning = None
        else:
            self.returning = x
        finally:
            self.root.quit()

    def to_clip(self, event=None):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.msg)


def mbox(msg, b1='OK', b2='Cancel', frame=True, t=False, entry=False,
         dropbox=False, elements=None, win_title='Message'):
    # Create an instance of MessageBox, and get data back from the user.
    # msg = string to be displayed
    # b1 = text for left button, or a tuple (<text for button>,
    # <to return on press>)
    # b2 = text for right button, or a tuple (<text for button>,
    # <to return on press>)
    # frame = include a standard outerframe: True or False
    # t = time in seconds (int or float) until the msgbox automatically closes
    # entry = include an entry widget that will have its contents returned:
    # True or False
    # dropbox = include a Combobox widget, choice will be returned: True or
    # False
    # elements  = items to be populated in dropbox: list
    # win_title = title on the window

    msgbox = MessageBox(msg, b1, b2, frame, t, entry, dropbox, elements,
                        win_title)
    msgbox.root.mainloop()
    # the function pauses here until the mainloop is quit
    msgbox.root.destroy()
    return msgbox.returning


# Tests - Run this file by itself to run the various tests below
if __name__ == "__main__":

    # define a function to be repeated at the end of every test that allows the
    # user to exit testing before it has finished.
    def pause():
        try:
            input("[*] Press ENTER to continue or Ctrl + c to exit.\n")
        except KeyboardInterrupt:
            print('\n[*] Tests interrupted, exiting')
            sys.exit()

    # --------------- #
    # One button test #
    # --------------- #
    print('[*] Running test 1 - Ok only\n')
    # This box should contain one button and return the value True
    test1_box = mbox('Press "OK" to continue', b2=False, win_title='Test 1')
    print(f'[*] Test 1 returned, {test1_box}\n')

    pause()

    # -------------- #
    # OK/CANCEL test #
    # -------------- #
    print('[*] Running test 2 - ok, cancel\n')
    # This box should return either True (if ok is selected) or false (if
    # cancel is selected).
    test2_box = mbox('Press "OK" or "Cancel"', win_title='Test 2')
    print(f'[*] Test 2 returned:  {test2_box}\n')

    pause()

    # ----------------- #
    # Button Tuple Test #
    # ----------------- #
    print('[*] Running test 3 - Button Tuple\n')
    # This box will return either "OK" (if ok is selected) or "Cancel" (if
    # cancel is selected).
    test3_box = mbox('Press "OK" or "Cancel"', b1=('OK', 'OK'),
                     b2=('Cancel', 'Cancel'), win_title='Test 3')
    print(f'[*] Test 3 returned:  {test3_box}\n')

    pause()

    # ----------------- #
    # Entry Widget Test #
    # ----------------- #
    print('[*] Running test 4 - Entry Widget\n')
    # This window will incorporate an entry widget and return the contents of
    # the entry widget.
    test4_box = mbox('Enter something and press ok', entry=True,
                     win_title='Test 4')
    print(f'[*] Test 4 returned:  {test3_box}\n')

    pause()

    # ------------------- #
    # Dropbox Widget Test #
    # ------------------- #
    print('[*] Running test 5 - Dropbox Widget\n')
    # This window will incorporate a dropbox widget and return the selected
    # option.
    test5_box = mbox('Please make a selection', dropbox=True,
                     elements=('Option1', 'Option2', 'Option3'),
                     win_title='Test 5')
    print(f'[*] Test 5 returned: {test5_box}\n')

    pause()

    # ---------- #
    # Timer Test #
    # ---------- #
    print('[*] Running test 6 - Timeout test\n')
    # This window will make use of the time out feature - wait 5 seconds and it
    # will close itself
    test6_box = mbox('Please wait 5 seconds for window to close', t=5,
                     win_title='Test 6')
    print(f'[*] Test 6 returned:  {test6_box}\n')
