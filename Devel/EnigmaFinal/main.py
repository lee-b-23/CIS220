"""
Name:  main.py
Author:  Lee Brown
Created:  10/22/2020
Last Updated:  11/01/2020
Purpose:  This is the main module for my enigma machine program.
Description: See purpose.
Sources:
 - https://www.geeksforgeeks.org/create-a-directory-in-python/
"""
import os
from datetime import date
import traceback
import EnigmaMachine
import ShowScreen as screen
import FileToList as ftl

def write_to_file(directory, data):
    if os.path.isfile(directory):
        count = 0
        while(True):
            #Adds slashes to make sure that they are there.  It doesn't seem to matter if there are four.
            location = directory +  '\\' + str(date.today()) + '(' + str(count) + ').txt'
            try:
                os.rename(location, location)
            except:
                save_file = open(location, 'w+')
                save_file.write(data)
                return True
            count += 1
    else:
        return False

def main():
    enigma = EnigmaMachine.EnigmaMachine()
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
        #1:  Encode Message
        if(value == '1'):
            error = 0
            value2 = stat.show_screen('encrypt_message')

            #do something with value2
            num = []
            if value2 == '':
                location = stat.show_screen('encrypt_message_file')
                data = ftl.read_to_list(location)[0]
                enigma.encode_message(data)
            store = enigma.encode_message(value2)
            print_store = store.split('\n')

            #See how many lines are going to be put on the screen.
            for x in range(0, len(print_store)):
                num.append('<l' + str(x + 1) + '>')
            
            #Show user the result and give option to save to a file.
            value3 = stat.show_screen('message_result', num, print_store)
            while value3 != 'e' and value3 != '':
                write_file = write_to_file(value3, store)
                if write_file == False:
                    value3 = stat.show_screen('message_result_fail', num ,print_store)
                else:
                    value3 = stat.show_screen('save_success')
                    break
        
        #2:  Decode Message
        elif(value == '2'):
            num = []
            error = 0
            value2 = stat.show_screen('decrypt_message')

            #do something with message
            store = enigma.decode_message(value2)
            print_store = store.split('\n')
            for x in range(0, len(print_store)):
                num.append('<l' + str(x + 1) + '>')
            
            value3 = stat.show_screen('message_result', num, print_store)
            while value3 != 'e' and value3 != '':
                write_file = write_to_file(value3, store)
                if write_file == False:
                    input('here')
                    value3 = stat.show_screen('message_result_fail', num ,print_store)
                else:
                    input("Maybe here")
                    value3 = stat.show_screen('save_success')
                    break
        
        #3:  About Screen
        elif(value == '3'):
            error = 0
            value2 = stat.show_screen('about')
        #4:  Exit
        elif(value == '4'):
            error = 0
            break
        else:
            #incorrect input option
            error = 1
    stat.show_screen('exit')
main()