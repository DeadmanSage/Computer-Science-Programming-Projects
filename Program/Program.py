
from email import message
from random import choice
import tkinter
from tkinter import *
import tkinter.font as font
import tkinter.messagebox
import time
import hashlib
from hashlib import sha256
import Inventory
from Inventory import InventoryReader
import csv

LoginScreen = None
BackColour = "#b3b1b1" # set the bakcground colour as a variable since it will be easier to call and make programming faster
Toplevel = ""
w = None
file = None

global username
global password
global username_check
global password_check

#testing with tkinter to see how to make a basic window

#def messageCall():
#    tkinter.messagebox.showinfo("hello world", "hello world")
#screen = tkinter.Tk()
#myfont = font.Font(family = 'american typewriter') #creates a font variable to be used
#screen.geometry("250x250") #window size
#screen.title("window title") #window title
#b = tkinter.Button(screen, text="Click here", font = myfont, bd = 7, fg = 'blue', activeforeground = 'red', height = 2, command = messageCall) #creates a button variable
#b.place(relx = 0.5, rely = 0.5, anchor = CENTER) #places the button variable
#screen.mainloop() #required to start instructions

# creating the main screen, will be used to greet users to the appication before logging in


def LoginSystem():
    
      


    LoginScreen = tkinter.Tk()
    LoginScreen.config(bg=BackColour) # setting the background colour
    LoginScreen.title("Sign into Account") # window title
    LoginScreen.geometry("500x500")
    LoginScreen.maxsize(500, 500)
    LoginScreen.minsize(500, 500)
     # window size
    #makes a screen for login

   

    global password
    global username
    global file
#username entry
    Label(LoginScreen, text="Login with school account to continue", bg="white", width="30",height="1", font=("Calibri", 10)).place(relx=0.3,rely=0.5, anchor=CENTER)
    Label(LoginScreen, text="Username ").pack()
    global username_entry
    username_entry = Entry(LoginScreen)
    username_entry.pack()
    Label(LoginScreen, text="").pack()
#password entry
    Label(LoginScreen, text="Password ").pack()
    global password_entry
    password_entry = Entry(LoginScreen,show = "*")
    password_entry.pack()
    Button(text="Login", height=2, width=20, command=Login,).place(relx=0.3,rely=0.8, anchor=CENTER)
    Button(text="quit", foreground='#7a0909', command=lambda:[LoginScreen.destroy, recommending()], height=2, width=20,).pack()
    time.sleep(2)
    
    #file = r"C:\Users\stu-dyer.b\OneDrive - Brighter Futures Learning Partnership Trust\Documents\GitHub\Computer-Science-Programming-Projects\Program\Login.txt"
    file = r"C:\Users\Biowa\Desktop\Computer-Science-Programming-Projects\Program\Login.txt"

    LoginScreen.mainloop()






def Login():
    hash_username = (username_entry.get()).encode()
    hash_password = (password_entry.get()).encode()
    print( sha256(hash_username).hexdigest())
    print( sha256(hash_password).hexdigest())

#print("SHA-256:", hashlib.sha256(message).hexdigest())

# going to put this system on hold while i focus on my recommendation system

def recommending():
    global w

    InventoryScreen = tkinter.Tk()
    InventoryScreen.config(bg=BackColour) # setting the background colour
    InventoryScreen.title("") # window title
    InventoryScreen.geometry("1920x1080")
    InventoryScreen.maxsize(1920,1080)
    InventoryScreen.minsize(1920,1080)


    # scrollbar = Scrollbar(InventoryScreen)
    # scrollbar.pack( side = RIGHT, fill = Y )

    # InvList = Listbox(InventoryScreen, yscrollcommand= scrollbar.set )
    # for line in range(100):
    #    InvList.insert()

    # list = []
    # for row in Inventory:
    #     list.append(row.get('Name'))
    # print(list)
    dropdown = []


    for row in Inventory.temp: # getting error saying object is not iterable
        print(row.get("Name") + " " + row.get("UC"))
        dropdown.append((row.get('Name') + " " + row.get('UC')))

    scrollbar = Scrollbar(InventoryScreen)
    #InvList = Listbox(InventoryScreen, yscrollcommand= scrollbar.set )
    def display_selected(choice):
        choice = listdef.get()
        print(choice)
        Choice(choice)

    def Choice(displayChoice):
        # if the selected item isnt available, it will search once for the tag for its category
        # it will then search all the csv for items with the same tag and add them to a list to be printed as a recommended alternative
        SimilarItems = []
        filteredList = []
        print(displayChoice)
        #GetUC = displayChoice[displayChoice.rindex(' ')]
        GetUC = int(displayChoice.rsplit(' ')[-1])
        print(GetUC)
        #getUC is integer


        # with open(file) as f:

            # FileReader = csv.reader(f)
            # FileArray = list(FileReader)
            # for row in FileArray:
            #     print(row)
            #     print(FileArray)
<<<<<<< Updated upstream
        File = r'Program\Inventory.csv'
=======

        #File = r'Program\Inventory.csv'
        File = r"C:\Users\Biowa\Desktop\Computer-Science-Programming-Projects\Program\Inventory .csv"
>>>>>>> Stashed changes
        with open(File) as f:
            FileReader = csv.reader(f)
            FileArray = list(FileReader)
            j = next(filter(lambda obj: obj.get('UC') == str(GetUC), FileArray), None)
            print(j)
            #print(FileArray)
        #    for row in FileArray:
        #        if row[3] == GetUC:
        #            filteredList.append(row)
        #    print(filteredList)




            
#item = next(iter(filter(lambda x: x['name'] == name, items)), None)
#use this to fix it


    listdef = StringVar(InventoryScreen)
    listdef.set(dropdown[0])
    w = OptionMenu(InventoryScreen, listdef, *dropdown, command=display_selected)
    w.pack()


    InventoryScreen.mainloop()

def getBox():
    global w
    print(w.get())



             
        


LoginSystem()   

#recommending() 