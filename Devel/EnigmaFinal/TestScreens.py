"""
Name:  ShowScreen.py
Author:  Lee Brown
Created:  10/22/2020
Last Updated:  10/22/2020
Purpose:  Shows a given screen for my Enigma Machine.
Description:  This program will display a screen from a text document in a
              command window.  It will need to clear that window first, and it
              will take in the given screen as parameters.
"""
import os
import FileToList as f
import ShowScreen as s

while(True):
    s.show_screen(input("Type screen name here: "))

    value = input("Again?  ")
    if value == 'y':
        continue
    else:
        break
