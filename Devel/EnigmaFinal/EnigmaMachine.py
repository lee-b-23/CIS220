"""
Name:  EnigmaMachine.py
Author:  Lee Brown
Created:  11/11/2020
Last Updated:  10/31/2020
Purpose:  This is going to be the base file for my entire enigma machine.
Description:  At the very least, this file will contain the interface through
            which the client creates and interacts with an enigma machine
            instance.
"""
import IsFactor as fact

class EnigmaMachine:
    #This is the interface for the enigma machine.  It will only contain user-level interactions with the machine.
    def __init__(self):
        self.enigma_machine = enigma_machine_class()
    def encode_message(self, message):
        store = self.enigma_machine.encode_message(message)
        return store
    def decode_message(self, message):
        store = self.enigma_machine.decode_message(message)
        return store

class enigma_machine_class:
    class plugboard:
        def __init__(self):
            pass
    class gear:
        def __init__(self):
            pass
    def __init__(self):
        #create gear and plugboard objects here
        #create variables for input and output
        pass
    
    #this method formats a message into or deformats it from the 5 character "words" and 5 word paragraphs format.
    def format_message(self, mode, message):
        new_message = ''
        if mode == 'e':
            count = 0
            #NOTE:  Adjust the math in the following if and elif statements to reflect the pattern that you are using.
            for x in message:
                if count == 6 or count == 12 or count == 18 or count == 24 or count == 30:
                    count += 1
                    new_message = new_message + ' '
                elif count == 36:
                    count = 0
                    new_message = new_message + "\n"
                    count += 1
                else:
                    count += 1
                new_message = new_message + x
            return(new_message)
        
        #If they choose to decode the message.
        elif mode == 'd':
            message.replace('\n', '')
            decrypted_message = ''
            count = 1
            for x in message:
                if fact.is_factor(count, 7) and count != 0:
                    pass
                else:
                    decrypted_message = decrypted_message + x
                count += 1
            return decrypted_message
        else:
            raise Exception("Incorrect mode used in format_message.")
    
    def encode_message(self, message):
        #<<do something with the message>>:
        #<<encrypt message>>
        new_message = self.format_message('e', message)
        return new_message
    def decode_message(self, message):
        #<<do something with the message>>:
        new_message = self.format_message('d', message)
        #<<decrypt message>>
        return new_message

'''value = enigma_machine_class()
value.format_message('e', 'message')'''