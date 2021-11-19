---
layout: default
title: Tkinter GUI Example
---

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
  - Implement logging throughout the application
- Create documentation
  - Annotations throughout source code
  - Utilize GitHub Pages
  - Explanation of aplication structure
  - Explanation of tabs
- Find a "stopping point" - call it "done"

One could spend an endless amount of time in the pursuit of perfection so it is important to impose limitations and cut scope as much as possible. I have many aspirations and lots in the backlog already so I'm trying to not get-out-of-hand with updating this older project.

## Application Overview

This application doesn't have a concise purpose aside from being a teaching tool and reference.

### Application Tabs

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

## Credits and Resources

Nothing in this world is possible without the assistance of others - special thanks to all those who made this project possible in some way! Please see below for a list of references (in no particular order) that have aided me in the journey that is this project.

- [Python interface to Tcl/Tk](https://docs.python.org/3/library/tkinter.html)
- [Python logging handlers documenation](https://docs.python.org/3/library/logging.handlers.html)
- [TkDocs](https://tkdocs.com/)
