from tkinter import *
from datetime import datetime


def test():
    window = Tk()
    
    #Creating and packing a label onto the screen.
    value = str(datetime.today())
    hello = Label(window, text=value)
    hello.pack()
    
    window.mainloop()

def basicButton():
    #make my window
    value = 0
    
    window = Tk()
    title = Label(window, text="Enigma Machine", underline='0')
    title.pack()
    label = Label(window, text="Type a message in the text box below.  Press the button when you are ready to encode it.  Your encoded message will appear in a second text box below.")
    label.pack()

    inputName = Entry(window)
    inputName.pack()
    inputName.insert(0, "Enter text here")
    result = Label(window, text="Results")
    resultEntry = Entry(window)
    resultEntry.pack()
    
    def buttonPress():
        #https://stackoverflow.com/questions/2260235/how-to-clear-the-entry-widget-after-a-button-is-pressed-in-tkinter
        resultEntry.delete(0, "end")
        resultEntry.insert(0, inputName.get())
    button = Button(window, text="Enter", command=buttonPress)
    button.pack()

    window.mainloop()

basicButton()
