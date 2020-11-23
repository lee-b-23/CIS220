"""
Name:  ShowScreen.py
Author:  Lee Brown
Created:  10/22/2020
Last Updated:  11/20/2020
Purpose:  Shows a given screen for my Enigma Machine.
Description:  This program will display a screen from a text document in a
              command window.  It will need to clear that window first, and it
              will take in the given screen as parameters.
Sources:
 - https://stackoverflow.com/questions/18262293/how-to-open-every-file-in-a-folder
 - https://stackoverflow.com/questions/4813061/non-alphanumeric-list-order-from-os-listdir
"""
import os
import FileToList as f
import time


class AbstractScreen:
    def __init__(self, directory, file_extention):
        self.dir = directory   #top level file for screens
        self.ext = file_extention   #type of file the screens are stored in
    def get_screen(self, name, folder = ''):
        if self.ext not in name:
            if folder == '':
                scr = f.read_to_list(self.dir + '\\' + name + self.ext)
            else:
                scr = f.read_to_list(self.dir + '\\' + folder + '\\' + name + self.ext)
            
        else:
            if folder == '':
                scr = f.read_to_list(self.dir + '\\' + name)
            else:
                scr = f.read_to_list(self.dir + '\\' + folder + '\\' + name)
        return scr
    
    #this is the part that will be modified by a subclass
    def show_screen(self):
        #raise "This is an abstract class.  Use a more concrete representation."
        pass

class StaticInputScreen(AbstractScreen):
    def show_screen(self, name, replace_what = [], replace_with = []):
        os.system('cls')
        scr = self.get_screen(name)

        count = 0
        for x in scr:
            if count != 0:
                if replace_with != []:
                    for y in range(0, len(replace_with)):
                        x = x.replace(replace_what[y], replace_with[y])
                if count == 23:
                    value = input(x)
                else:
                    print(x)
            count = count + 1
        return value

class AnimatedScreen(AbstractScreen):
    def show_screen(self, folder_name):
        os.system('cls')
        names = os.listdir(self.dir + '\\' + folder_name)
        names.sort()
        for name in names:
            os.system('cls')
            scr = self.get_screen(name, 'loading')

            count = 0
            for x in scr:
                if count != 0:
                    print(x)
                else:
                    pass
                count = count +1
            time.sleep(0.25)
            
class ShowScreen:
    #This is the interface for the screen showing module
    def __init__(self, directory, screen_extention):
        self.static_scr = StaticInputScreen(directory, screen_extention)
        self.animated_scr = AnimatedScreen(directory, screen_extention)
    
    def show_screen(self, scr_type, name = '', replace_what = [], replace_with = [], folder = ''):
        if scr_type == 'static':
            return self.static_scr.show_screen(name, replace_what, replace_with)
        elif scr_type == 'animated':
            return self.animated_scr.show_screen(folder)
        else:
            #raise "Incorrect screen type specified."
            pass

'''value = ShowScreen('D:\\CIS220\\Devel\\EnigmaFinal\\screens', '.txt')
value.show_screen('animated', '','loading')'''


'''screen = AnimatedScreen('D:\\CIS220\\Devel\\EnigmaFinal\\screens', '.txt')
screen.show_screen('loading')
screen2 = StaticInputScreen('D:\\CIS220\\Devel\\EnigmaFinal\\screens', '.txt')
screen2.show_screen('main_menu')'''
