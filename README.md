# Tkinter GUI Example

An example Python application that utilizes the tkinter library to create a Graphical User Interface.

## Synopsis

This project is a tabbed, tkinter, GUI application intended to be a reference for future applications (e.g., a "starting point") and demonstrate my own learning. The intent of the application is to demontsrate as many capabilities of tkinter while utilizing some design patterns and practices.

## Getting started

Running this application is as simple as cloning the repository and invoking `launch-application.py`!

## Current status

- Restructured application to model it more closely resemble the application factory utilized by [Flask projects](https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/)
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
