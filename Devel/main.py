"""
Name: main.py
Author:  Lee Brown
Created:  10/08/2020
Last Updated:  10/10/2020
Purpose:  Creating the main menu for my enigma machine program.
Description:  
"""


def plugBoard():
    pass
def gearOrder():
    pass
def gearConfig():
    pass
def mainMenu():
    #This will be the area that will contain all of the objects that are from the machine class.
    
    
    
    print("--------------------------Enigma Machine--------------------------")
    print("Welcome to Enigma Machine!  It is important that you and your message receiver are using the same version of machine so that gear rotations will match.")
    print("")
    a = input("Would you like to use the machine?  Type 'yes' or 'no'>>>  ")
    print("")
    while(a.lower().strip() == "y" or a.lower().strip() == "yes" or a.lower().strip() == "again"):
        print("-------------------------------------------------------------------------------")
        print("<<<Menu>>>")
        print("#Note:  Machine configuration will remain until reset via the menu below.")
        print(" (1)  Configure plugboard")
        print(" (2)  Set Gear Order")
        print(" (3)  Configure Gears")
        print(" (4)  Encode Message")
        print(" (5)  Reset Machine")
        print(" (6)  Exit")
        print("")
        b = input("Type the number of an option above>>>  ")
        print("")
        if (b.lower().strip() == "1"):
            #Plugboard Menu
            pass
        elif (b.lower().strip() == "2"):
            #Gear Order Menu
            c = "yes"
            d = ['0', '0', '0']
            while(c.lower().strip() == "yes" or c.lower().strip() == "y"):
                print("There are three gears (1, 2, and 3) and three positions (1, 2, and 3) for them to be placed in.")
                print("Follow the prompts to place each gear in its desired location.")
                print("Gears to be Placed:  (1, 2, 3)")
                print("Positions to Fill:   (1, 2, 3)")
                d[0] = input("Type desired position of gear 1>>>  ")
                print(">>>Position Entered")
                d[1] = input("Type desired position of gear 2>>>  ")
                print(">>>Position Entered")
                d[2] = input("Type desired position of gear 3>>>  ")
                print(">>>Position Entered")
                print("")

                #>>>TEST INPUT HERE
                c = input("Would you like to reorder the gears? 'y' or 'n'>>>  ")
                c = c
                
                #>>>If input passes the test and is final, submit it to the machine.
                
            pass
        elif (b.lower().strip() == "3"):
            #Configure Gears Menu
            c = "yes"
            d = [0, 0, 0]
            while(c.lower().strip() == "yes" or c.lower().strip() == "y"):
                print("Follow the prompts below to rotate the gear at each position (1, 2, and 3) a certain amount of times...")
                d[0] = input("Type desired position of gear 1>>>  ")
                print(">>>Gear Rotated")
                d[1] = input("Type desired position of gear 2>>>  ")
                print(">>>Gear Rotated")
                d[2] = input("Type desired position of gear 3>>>  ")
                print(">>>Gear Rotated")
                print("")

                #>>>TEST INPUT HERE
                
                c = input("Would you like to reorder the gears? 'y' or 'n'>>>  ")
                c = c

                #>>>If input passes the test and is final, submit it to the machine.
                
        elif (b.lower().strip() == "4"):
            #Encode Message Menu
            message = input("Type message here>>>  ")
            #>>>RETURN MESSAGE ENCODED
            
        elif(b.lower().strip() == "5"):
            #Reset Machine
            #>>>USE RESET FUNCTION TO RESET THE MACHINE
            pass
        elif(b.lower().strip() == "6"):
            #Quit
            break
        else:
            print("ERROR:  Incorrect input.")

        print("")
        a = input("Would you like to return to the menu?>>>  ")
        a = a
        print("")

    print("")
    print("Thank you for using Enigma Machine!")
mainMenu()
