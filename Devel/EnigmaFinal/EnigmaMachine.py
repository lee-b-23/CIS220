"""
Name:  EnigmaMachine.py
Author:  Lee Brown
Created:  10/31/2020
Last Updated:  12/06/2020
Purpose:  This is going to be the base file for my entire enigma machine.
Description:  At the very least, this file will contain the interface through
            which the client creates and interacts with an enigma machine
            instance.
Notes:
 - the set methods for the inbound and outbound character are necessary because the number of gears that the program will use is unknown.
 - There is no random generation of character sets.  There is not way to decode such messages.
 - The user does not choose the gear configurations.  Anyone who has access to the actual code can.  As Ed noted, it is pointless to make the
   user communicate to their receiver about the specific settings of the machine like the Germans did.

Sources:
 - https://stackoverflow.com/questions/20844347/how-would-i-make-a-custom-error-message-in-python
 - https://theasciicode.com.ar/ascii-printable-characters/ampersand-ascii-code-38.html
 - https://www.w3schools.com/python/python_howto_reverse_string.asp
"""
import IsFactor as fact

class EnigmaMachine:
    #This is the interface for the enigma machine.  It will only contain user-level interactions with the machine.
    def __init__(self):
        self.enigma_machine = enigma_machine_class()
    def encode_message(self, message):
        try:
            store = self.enigma_machine.encode_message(message)
            return store
        except:
            raise ValueError("Bad input character(s).")
    def decode_message(self, message):
        try:
            store = self.enigma_machine.decode_message(message)
            return store
        except:
            raise ValueError("Bad input character(s).")





class enigma_machine_class:
    #encryption is the inbound side, decryption is the outbound side.  If encrypting, the inbound side is replaced by the outbound side.
    class plugboard:
        def __init__(self):
            self.__inbound__ = ['<', '!', '"', '&', '(', ')', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '?', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '‚', '„']
            self.__outbound__ = ['C', 'j', 'z', 'k', 's', 'l', 'T', 'N', 'Z', 'R', 'u', 'M', 'K', 'Q', 'E', 'f', 'B', 'g', 'H', 'X', 'A', 'a', 'x', '&', 'p', 'D', 'q', 'm', '.', 'i', 't', '(', 'd', 'L', ')', 'w', 'y', 'o', '!', '5', 'e', 'S', '<', 'b', '2', 'W', '‚', 'P', 'V', '„', '0', 'F', '9', 'v', '8', 'Y', 'G', '7', 'r', 'n', '1', 'J', 'I', 'O', 'h', 'c', '6', '4', '?', 'U', '3', '"']
        def get_index(self, char):
            for x in range(0, len(self.__inbound__)):
                if self.__inbound__[x] == char:
                    return x
        def encrypt(self, message):
            new_message = ''
            for char in message:
                if char in self.__inbound__:
                    index = self.get_index(char)
                    new_message += self.__outbound__[index]
            return new_message
        def decrypt(self, message):
            new_message = ''
            for char in message:
                if char in self.__outbound__:
                    index = self.get_index(char)
                    new_message += self.__inbound__[index]
            return new_message
        
    class gear_box:
        class gear:
            def __init__(self):
                self.__gear__ = []
                self.__outbound__ = []
            def rotate(self, direction):
                temp = []
                if direction == 'forward':
                    temp.append(self.__gear__[-1])
                    for x in range(0, len(self.__gear__) - 1):
                        temp.append(self.__gear__[x])
                    self.__gear__ = temp
                elif direction == 'backwards':
                    for x in range(1, len(self.__gear__)):
                        temp.append(self.__gear__[x])
                    temp.append(self.__gear__[0])
                    self.__gear__ = temp
            def set_gear(self, gear_list):
                self.__gear__ = gear_list
            def get_char(self, index):
                return self.__gear__[index]
            def get_index(self, character):
                for x in range(0, len(self.__gear__)):
                    if self.__gear__[x] == character:
                        return x
        def __init__(self):
            #create the four gears
            self.__gear1__ = self.gear()
            self.__gear1__.set_gear(['M', '6', 'G', 'X', 'H', 'L', 'p', '<', 'd', '‚', 'E', '5', 'Q', 'f', 'g', 'Y', '4', 'O', '.', 'A', 'K', 'r', '?', 'S', '9', 'i', 'b', 'n', 'D', 'z', '(', '7', 'B', 'v', 'x', '!', 'N', ')', 'T', 'a', 'R', 'h', 'V', 'u', 'y', 'Z', '2', '1', 'F', 'j', 'm', 'P', 's', '&', 'l', 'q', 't', 'W', 'k', 'J', '"', 'e', 'I', 'c', 'U', 'o', '8', '„', 'C', '3', '0', 'w'])

            self.__gear2__ = self.gear()
            self.__gear2__.set_gear(['!', 'W', 'p', ')', 'g', 's', '1', 'l', 'S', 'G', '4', 'n', 'b', 'o', '2', '3', 'X', 'P', 'a', 'O', 'u', 'U', 'C', 'Q', 'x', 'm', '7', '"', '(', '9', '‚', 'v', 'F', 'z', '&', '6', '8', 'V', 'R', 'h', 'i', 'Y', 'J', 'H', 'c', 'L', '0', 'q', 'f', 'd', 'y', 'j', 'I', 'Z', '.', 'B', 'w', 'M', 'e', 'K', 'D', 'A', 't', 'r', 'E', '?', '<', '5', '„', 'k', 'N', 'T'])
            
            self.__gear3__ = self.gear()
            self.__gear3__.set_gear(['V', 'E', 'g', '5', 's', 'H', 'r', 'P', 'a', '7', 't', 'e', 'D', 'W', 'v', 'h', '9', '4', 'f', 'i', 'S', '„', '"', '‚', 'p', 'q', 'T', 'Q', 'm', 'M', '0', 'Y', 'J', 'z', 'G', '1', '!', '(', 'u', '<', 'B', 'F', 'c', '&', 'l', 'I', 'U', 'd', 'k', 'w', '8', '.', 'O', '3', 'o', 'n', 'L', 'A', 'K', ')', 'R', '2', 'Z', 'b', 'C', 'N', 'x', 'X', '?', '6', 'j', 'y'])
            
            self.__gear4__ = self.gear()
            self.__gear4__.set_gear(['e', 'P', 'T', '1', 'n', 'f', 'J', '„', 'G', 't', 'O', 'l', 'a', '5', 'D', 'K', '(', 'r', 'z', 'B', 'b', '6', 'd', '&', 'w', 'L', 'Z', 'x', 'm', 'H', 'N', 'j', '2', '"', 'V', 'c', '7', 'F', 'u', '0', 'E', 'k', '.', 'p', 'g', 'o', 'X', 'M', 'Q', '3', 'A', '4', 'I', 's', 'h', '!', 'i', 'y', ')', '?', 'v', 'U', 'R', '‚', 'q', 'Y', '8', 'W', 'C', '9', 'S', '<'])

            self.og1 = self.__gear1__
            self.og2 = self.__gear2__
            self.og3 = self.__gear3__
            self.og4 = self.__gear4__
        def reset_gears(self):
            self.__gear1__.set_gear(['M', '6', 'G', 'X', 'H', 'L', 'p', '<', 'd', '‚', 'E', '5', 'Q', 'f', 'g', 'Y', '4', 'O', '.', 'A', 'K', 'r', '?', 'S', '9', 'i', 'b', 'n', 'D', 'z', '(', '7', 'B', 'v', 'x', '!', 'N', ')', 'T', 'a', 'R', 'h', 'V', 'u', 'y', 'Z', '2', '1', 'F', 'j', 'm', 'P', 's', '&', 'l', 'q', 't', 'W', 'k', 'J', '"', 'e', 'I', 'c', 'U', 'o', '8', '„', 'C', '3', '0', 'w'])
            self.__gear2__.set_gear(['!', 'W', 'p', ')', 'g', 's', '1', 'l', 'S', 'G', '4', 'n', 'b', 'o', '2', '3', 'X', 'P', 'a', 'O', 'u', 'U', 'C', 'Q', 'x', 'm', '7', '"', '(', '9', '‚', 'v', 'F', 'z', '&', '6', '8', 'V', 'R', 'h', 'i', 'Y', 'J', 'H', 'c', 'L', '0', 'q', 'f', 'd', 'y', 'j', 'I', 'Z', '.', 'B', 'w', 'M', 'e', 'K', 'D', 'A', 't', 'r', 'E', '?', '<', '5', '„', 'k', 'N', 'T'])
            self.__gear3__.set_gear(['V', 'E', 'g', '5', 's', 'H', 'r', 'P', 'a', '7', 't', 'e', 'D', 'W', 'v', 'h', '9', '4', 'f', 'i', 'S', '„', '"', '‚', 'p', 'q', 'T', 'Q', 'm', 'M', '0', 'Y', 'J', 'z', 'G', '1', '!', '(', 'u', '<', 'B', 'F', 'c', '&', 'l', 'I', 'U', 'd', 'k', 'w', '8', '.', 'O', '3', 'o', 'n', 'L', 'A', 'K', ')', 'R', '2', 'Z', 'b', 'C', 'N', 'x', 'X', '?', '6', 'j', 'y'])
            self.__gear4__.set_gear(['e', 'P', 'T', '1', 'n', 'f', 'J', '„', 'G', 't', 'O', 'l', 'a', '5', 'D', 'K', '(', 'r', 'z', 'B', 'b', '6', 'd', '&', 'w', 'L', 'Z', 'x', 'm', 'H', 'N', 'j', '2', '"', 'V', 'c', '7', 'F', 'u', '0', 'E', 'k', '.', 'p', 'g', 'o', 'X', 'M', 'Q', '3', 'A', '4', 'I', 's', 'h', '!', 'i', 'y', ')', '?', 'v', 'U', 'R', '‚', 'q', 'Y', '8', 'W', 'C', '9', 'S', '<'])
        def encrypt(self, message):
            #my plan is for the first gear to rotate every character, the second every 5 chars, the third every 25 chars, the fourth every 125 chars, etc.
            new_message = ''
            rotations = 0
            for char in message:
                #even though it is basically useless
                try:
                    char = self.__gear1__.get_index(char)
                    char = self.__gear4__.get_char(char)                   #this try-except block is to void bad characters
                    new_message += char
                    self.__gear1__.rotate('forward')
                    rotations += 1
                except:
                    pass
            self.reset_gears()
            return new_message
        def decrypt(self, message):
            new_message = ''
            temp = ''
            rotations = 0
            for char in message:
                if char in self.__gear1__.__gear__:
                    self.__gear1__.rotate('forward')
                    rotations += 1
                else:
                    input("HERE")
            self.__gear1__.rotate('backwards')
            rotations -= 1                                            #this makes it so that the rotations are at 0
            for x in range(len(message) - 1, -1, -1):
                try:
                    temp = self.__gear4__.get_index(message[x])
                    temp2 = self.__gear1__.get_char(temp)
                    new_message += temp2
                    self.__gear1__.rotate('backwards')
                    rotations -= 1
                except:
                    pass                                             #this excepts bad characters by removing them

            self.reset_gears()
            new_message = new_message[::-1]
            return new_message
            #no need for a gear reset because they should be all back to where they started.
    def __init__(self):
        #create gear and plugboard objects here
        #create variables for input and output
        self.char_set = ['<', '!', '"', '&', '(', ')', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '?', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '‚', '„']
        self.__plugboard__ = self.plugboard()
        self.__gear_box__ = self.gear_box()
        

    #this method formats a message into or deformats it from the 5 character "words" and 5 word paragraphs format.
    def format_message(self, mode, message):
        new_message = ''
        if mode == 'e':
            count = 0
            #NOTE:  Adjust the math in the following if and elif statements to reflect the pattern that you are using.
            for x in message:
                if count == 6 or count == 12 or count == 18 or count == 24 or count == 30:
                    count += 1
                    new_message = new_message + '  '
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
            message = message.replace('\n', '')
            message = message.replace('  ', '')
            return message
        else:
            raise Exception("Incorrect mode used in format_message.")
    


    def encode_message(self, message):
        #replace spaces and newlines,
        # check for bad characers,
        #encrypt,
        #and format
        message = message.replace(' ', '<')
        message = message.replace('\n', '&')

        #put message through gears
        new_message = self.__plugboard__.encrypt(message)
        new_message = self.__gear_box__.encrypt(message)
        new_message = self.format_message('e', new_message)
        return new_message
    def decode_message(self, message):
        #deformat,
        #check for bad characters,
        #decrypt,
        #and replace < and % with SPACE and \n respectively

        #put message through gears
        new_message = self.format_message('d', message)

        #decode message
        new_message = self.__gear_box__.decrypt(new_message)
        new_message = self.__plugboard__.decrypt(new_message)
        new_message = new_message.replace('<', ' ')
        new_message = new_message.replace('&', '\n')
        return new_message