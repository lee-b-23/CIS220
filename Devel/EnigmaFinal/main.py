"""
Name:  main.py
Author:  Lee Brown
Created:  10/22/2020
Last Updated:  11/01/2020
Purpose:  This is the main module for my enigma machine program.
Description: See purpose.
"""

import ShowScreen as screen

def main():
    stat = screen.StaticInputScreen('D:\\CIS220\\Devel\\EnigmaFinal\\screens', '.txt')
    dyn = screen.AnimatedScreen('D:\\CIS220\\Devel\\EnigmaFinal\\screens', '.txt')

    stat.show_screen('welcome')
    
    error = 0
    while(True):
        #Test to see if incorrect input was found.  Display correct menu
        #accordingly.
        if(error == 0):
            value = stat.show_screen('main_menu')
        else:
            value = stat.show_screen('main_menu_incorrect')

        #Menu Options
        if(value == '1'):
            error = 0
            value2 = stat.show_screen('encrypt_message')
            #do something with value2
            value3 = stat.show_screen('message_result')
        elif(value == '2'):
            error = 0
            value2 = stat.show_screen('decrypt_message')
            value3 = stat.show_screen('message_result')
        elif(value == '3'):
            error = 0
            value2 = stat.show_screen('about')
        elif(value == '4'):
            error = 0
            break
        else:
            #incorrect input option
            error = 1
    stat.show_screen('exit')
main()
