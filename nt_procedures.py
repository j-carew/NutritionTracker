# nt_Procedures.py

# This module contains the main procedures for the project.

import curses
from nt_definitions import *

# Option 3 procedure
def addFood(stdscr):
    stdscr.clear()
    stdscr.addstr("Option 3\n")
    stdscr.addstr("This option is special")

    stdscr.refresh()

# curses.wrapper(addFood)
