# tkinterguiexample

An example of how to create a GUI using TKinter (packaged with Python).

## Synopsis

This project is a tabbed tkinter GUI intended to be a reference point for me (and others interested) to more efficiently create Python GUI applications. This is a personal project.

## Getting started

Running this application is as simple as cloning the repository and invoking `launch-application.py`!

## Current status

- Restructured application to model it more closely to a modern Flask app
  - All Application code in subdirectory `MyExampleApp`
  - App is created via construction function in the `__init__.py` file
- Added configuration object and established logging configuration
- Added custom icon

## To do

- Create observer pattern relationship between the primary and secondary tabs
- Add reactions/actions based on pop-up selection on button tab
- Add line numbering and "menu" icons to text entry tab

## Credits and Resources

- [Python interface to Tcl/Tk](https://docs.python.org/3/library/tkinter.html)
