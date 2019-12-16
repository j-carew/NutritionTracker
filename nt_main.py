#nt_main.py

# This file is the "engine" of the project.  It will interact with the user
# through the terminal to allow tracking of nutrition.  It will also allow
# changes to stored data of foods.

from nt_definitions import * # contains 'Food' class as well as functions to manipulate them
import curses # For altering terminal screens

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("--Welcome to Nutrition Tracker!--\n\n")

    stdscr.addstr("What would you like to do?\n\n")

    # The following string will be printed to the screen and ask the user to input
    # a number to perform a corresponding action.

    stdscr.addstr("[1] Check current nutrition counts\n"
          "[2] Update today's counts\n"
          "[3] Add info for a food\n"
          "[4] Edit info for a food\n"
          "[5] Exit Program\n")


    # The following section currently needs work
    choice = ''
    while choice != '5':

        choice = stdscr.getkey()

        if choice == '1':
            stdscr.clear()
            stdscr.addstr("Option 1")
        elif choice == '2':
            stdscr.clear()
            stdscr.addstr("Option 2")
        elif choice == '3':
            stdscr.clear()
            stdscr.addstr("Option 3")
        elif choice == '4':
            stdscr.clear()
            stdscr.addstr("Option 4")
        elif choice == '5':
            pass
        else:
            stdscr.addstr("Invalid option.  Please try again.\n")

    stdscr.refresh()

curses.wrapper(main)
