"""
Name:  main.py
Author:  Lee Brown
Created:  10/22/2020
Last Updated:  12/6/2020
Purpose:  This is the main module for my enigma machine program.
Description: See purpose.
Sources:
 - https://www.geeksforgeeks.org/create-a-directory-in-python/
         Used for os.path.exists()
 - https://www.codementor.io/tips/4043378291/why-does-python-os-path-isfile-return-false-on-windows-for-only-a-specific-directory
 - https://bugs.python.org/issue33105
 - https://www.geeksforgeeks.org/how-to-print-exception-stack-trace-in-python/
"""
import os
import traceback
import sys
from datetime import date
import traceback
import EnigmaMachine
import ShowScreen as screen
import FileToList as ftl

def write_to_file(directory, data):
    directory = os.path.abspath(directory)
    if os.path.exists(directory):
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
    screens = screen.ShowScreen('D:\\CIS220\\Devel\\EnigmaFinal\\screens', '.txt')

    screens.show_screen('static', 'welcome')
    
    error = 0
    while(True):
        #Test to see if incorrect input was found.  Display correct menu
        #accordingly.
        if(error == 0):
            value = screens.show_screen('static', 'main_menu')
        else:
            value = screens.show_screen('static', 'main_menu_incorrect')



        #Menu Options
        #OPTION 1
        #1:  Encode Message
        if(value == '1'):
            error = 0
            value2 = screens.show_screen('static', 'encrypt_message')   #original menu screen

            #check for bad characters and encode
            while(True):
                try:
                    #do something with value2
                    num = []
                    #file input handling
                    if value2 == '':
                        location = screens.show_screen('static', 'encrypt_message_file')
                        while location != 'e':
                            try:
                                data = ftl.read_to_list(location)
                                value2 = ''
                                for x in data:
                                    value2 = value2 + x
                                break
                            except:
                                location = screens.show_screen('static', 'encrypt_message_file_error')
                                if location == 'e':
                                    value2 = ''
                                    pass
                    location = ''
                    store = enigma.encode_message(value2)
                    break
                except ValueError:
                    input(traceback.print_exc())
                    value2 = screens.show_screen('static', 'encrypt_message_bad')

            if location != 'e':
                print_store = store.split('\n')
                #See how many lines are going to be put on the screen.
                for x in range(0, len(print_store)):
                    num.append('<l' + str(x + 1) + '>')
                num.append('<too_large>')
                if len(num) > 9:
                    print_store.append('Message too large.  Save entire message in a file.')
                else:
                    print_store.append('')
                for x in range(len(num), 10):
                    num.append('<l' + str(x) + '>')
                    print_store.append('')
                    
                #FILE WRITING SECTION
                value3 = screens.show_screen('static', 'message_result', num, print_store)
                while value3 != 'e' and value3 != '':
                    write_file = write_to_file(value3, store)
                    if write_file == False:
                        value3 = screens.show_screen('static', 'message_result_fail', num ,print_store)
                    else:
                        value3 = screens.show_screen('static', 'save_success')
                        break
            else:
                pass
        

        


        #OPTION 2
        #2:  Decode Message
        elif(value == '2'):
            num = []
            error = 0
            value2 = screens.show_screen('static', 'decrypt_message')

            #check for bad characters and decode
            while(True):
                try:
                    #file input handling
                    if value2 == '':
                        location = screens.show_screen('static', 'decrypt_message_file')
                        while location != 'e':
                            try:
                                data = ftl.read_to_list(location)
                                value2 = ''
                                for x in data:
                                    value2 = value2 + x
                                break
                            except:
                                location = screens.show_screen('static', 'decrypt_message_file_error')
                                if location == 'e':
                                    value2 = ''
                    location = ''
                    store = enigma.decode_message(value2)
                    break
                except ValueError:
                    input(traceback.print_exc())
                    value2 = screens.show_screen('static', 'decrypt_message_bad')
            

            if location != 'e':
                #do something with message
                print_store = store.split('\n')
                #See how many lines are going to be put on the screen.
                for x in range(0, len(print_store)):
                    num.append('<l' + str(x + 1) + '>')
                num.append('<too_large>')
                if len(num) > 9:
                    print_store.append('Message too large.  Save entire message in a file.')
                else:
                    print_store.append('')
                for x in range(len(num), 10):
                    num.append('<l' + str(x) + '>')
                    print_store.append('')
                #Show user the result and give option to save to a file.
                value3 = screens.show_screen('static', 'message_result', num, print_store)

                #FILE WRITING SECTION
                while value3 != 'e' and value3 != '':
                    write_file = write_to_file(value3, store)
                    if write_file == False:
                        value3 = screens.show_screen('static', 'message_result_fail', num ,print_store)
                    else:
                        value3 = screens.show_screen('static', 'save_success')
                        break
            else:
                pass
        
        #OPTION 3
        #3:  About Screen
        elif(value == '3'):
            error = 0
            value2 = screens.show_screen('static', 'about')

        #OPTION 4
        #4:  Exit
        elif(value == '4'):
            error = 0
            break
        else:
            #incorrect input option
            error = 1
    screens.show_screen('static', 'exit')
main()