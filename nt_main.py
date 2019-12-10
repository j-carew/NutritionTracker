# nt_main.py

# This file is the "engine" of the project.  It will interact with the user
# through the terminal to allow tracking of nutrition.  It will also allow
# changes to stored data of foods.

from nt_definitions import * # contains 'Food' class as well as functions to manipulate them

print("--Welcome to Nutrition Tracker!--")
print("What would you like to do?")
print("[1] Check current nutrition counts\n"
      "[2] Update today's counts\n"
      "[3] Add info for a food\n"
      "[4] Edit info for a food\n"
      "[5] Exit Program")

choice = input("Enter number of choice: ")

if choice == '1':
    print("good")
else:
    print("bad")
