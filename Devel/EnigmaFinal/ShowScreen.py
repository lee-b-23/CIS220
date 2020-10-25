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

def show_screen(screen):
    #os.system('cd D:\CIS210\Devel\FinalProject')
    os.system('cls')
    screen_file = ("screens\\" + screen + '.txt')
    screen_data = f.read_to_list(screen_file)
    count = 0
    for x in screen_data:
        if count != 0:
            if count == 23:
                value = input(x)
            else:
                print(x)
        count = count + 1
    return value
    

#show_screen('encode_message')
