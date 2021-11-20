---
layout: default
title: Tkinter GUI Example
---

[GitHub Repository](https://KyleEgland.github.com/tkinterguiexample)

# Tkinter GUI Example Application

A Python application written with the tkinter library to provide a GUI for this example project.

## Synopsis

This is an "evergreen" learning project meant to demonstrate Python, the tkinter GUI library, and my own capabilities. This project started as something to tinker with in order to isolate project specific code from its interface representation in order experiment. I was having issues with implemenation of certain tasks and found it nice to have a "clean reference". The Tkinter GUI Example has, since its initial creation, has been subjected to refactoring in order to present better code and practices. My intention is not to "get it right" but to make it better so that others may learn from what is here. I've also learned new practices and design patterns as well that I'd like to replicate in past projects to have better references (and starting points - D.R.Y.) for the future.

## Purpose

The purpose of this project is to provide a tabbed, tkinter-created, GUI application which offers examples of comman and basic GUI needs.

## Goals

- Create a tabbed tkinter-based GUI application
  - Create (3) distinct tabs to display the various capabilities of tkinter
  - Create a basic project structure (skeleton for future re-use)
  - Implement configuration (e.g. logging)
- Create documentation
  - Annotations throughout source code
  - Utilize GitHub Pages
  - Explanation of aplication structure
  - Explanation of tabs
- Find a "stopping point" - call it "done"

One could spend an endless amount of time in the pursuit of perfection so it is important to impose limitations and cut scope as much as possible in order to arrive at what one truly set out to do. I have many aspirations and lots in the backlog already so I'm trying to not get-out-of-hand with updating this older project.

## Application Overview

This application doesn't have a concise purpose aside from being a teaching tool and reference. Note that there is no shared data between the tabs and, while there is a "File" menu, it doesn't load anything (simply produces some pop-up windows). The configuration provided by the `config.py` file is mostly for logging setup. There is a configuration object which gets consumed by the application but it isn't serving a purpose so much as existing for future use/reference. This object is intended to hold environment variables that get passed into the application - configuration elements that are local and specific to the application's installation would be handled through here. I would, generally, use the package [python-dotenv](https://pypi.org/project/python-dotenv/) to achieve this (loading in of an environment file).

### Application Tabs

There are (3) distinct tabs because, why not three? It seemed the most appropriate number to demonstrate the notebook widget of tkinter. Each tab has a primary goal - depicted by its name - which may be comprised of one or more functions (methods on the tab's class) in order to achieve its objective(s).

**Timer Tab**

A countdown timer that takes an integer, supplied through the input widget, and counts down that many seconds (e.g. enter 60 into the text box to get a 1 minute timer). This tab is less a demonstration of how to do a timer and more of a demonstration of how to pass time in tkinter using the `.after()` method. This tab also demonstrates utilizing a text entry widget, and updating labels among some basic setup (e.g. grid layout).

![tkinterguiexample-timer-tab-drawing](/images/tkinterguiexample-Timer-Tab.drawio.svg)

**List Tab**

A demonstration of the listbox widget by allowing additions to a listbox and moving items between two listboxes. This tab has a rather complex layout and structure. The drawing tool ([draw.io](https://draw.io)) I used really helps to visual the application structure in order to code the layout properly - prevented scrolling up and down the code. This tab's code is relatively straight forward - the addition of text to a listbox is repeated from the Timer Tab and the code moving items is simply inverted.

![tkinterguiexample-list-tab-drawing](/images/tkinterguiexample-List-Tab.drawio.svg)

**Text Editor Tab**

An example of how to load file contents into tkinter. This tab utilizes the filedialog feature to load a text file's contents and allows the user to save modifications back to the same file name and location. Note that there is no file dialog opened for the save button - the text entry widgets contents are saved directly to the file that was loaded.

![tkinterguiexample-text-editor-tab-drawing](/images/tkinterguiexample-Text-Editor-Tab.drawio.svg)

### Project Structure

```
~/TKINTERGUIEXAMPLE/
.
├── docs/
│   └── Files for GitHub Pages (what you're reading)
├── MyExampleApp/
│   ├── src/
│   │   ├── icons
│   │   │   └── favicon.ico
│   │   ├── __init__.py
│   │   ├── ListTab.py
│   │   ├── TextEditorTab.py
│   │   └── TimerTab.py
│   ├── __main__.py
│   └── config.pyc
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

The layout of this project roughly mimics that of the [Flask application factory pattern](https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/). The `__main__.py` file builds the application that is started with the main window in the `__init__.py` file in the `~/MyExampleApp/src/` directory. The `MyAppWindow` object created in the `__init__.py` file is the "main window" of the example application. The individual tabs are imported here and "attached" to the notebook widget created inside the root window. Each tab has its own file that contains a class of the same name which is the frame (tab).

## Credits and Resources

Nothing in this world is possible without the assistance of others - special thanks to all those who made this project possible in some way! Please see below for a list of references (in no particular order) that have aided me in the journey that is this project.

- [Python interface to Tcl/Tk](https://docs.python.org/3/library/tkinter.html)
- [Python logging handlers documenation](https://docs.python.org/3/library/logging.handlers.html)
- [TkDocs](https://tkdocs.com/)
- [Opening File (Tkinter)](https://stackoverflow.com/questions/16429716/opening-file-tkinter)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/2e/chapter9/)
