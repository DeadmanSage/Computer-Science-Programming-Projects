
from email import message
import tkinter
from tkinter import *
import tkinter.font as font
import tkinter.messagebox
import time
import hashlib
from hashlib import sha256

LoginScreen = None
BackColour = "#b3b1b1" # set the bakcground colour as a variable since it will be easier to call and make programming faster
Toplevel = ""

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

    #username_check = StringVar()
    #password_check = StringVar()

    global password
    global username
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
    Button(text="quit", foreground='#7a0909', command=quit, height=2, width=20,).pack()
    time.sleep(2)
    
    file = r"C:\Users\stu-dyer.b\OneDrive - Brighter Futures Learning Partnership Trust\Documents\GitHub\Computer-Science-Programming-Projects\Program\Login.txt"
    LoginScreen.mainloop()

# We want to call the global variable code(below) when the button is pressed so that they are updated accordingly. 

    #username = username_entry.get()

    #password = password_entry.get()

    #print(username, password)

 #username = "username"
# password = "password"



def Login():
    hash_username = (username_entry.get()).encode()
    hash_password = (password_entry.get()).encode()
    print( sha256(hash_username).hexdigest())
    print( sha256(hash_password).hexdigest())

#print("SHA-256:", hashlib.sha256(message).hexdigest())

# going to put this system on hold while i focus on my recommendation system

def recc():
    Inventory = r"C:\Users\stu-dyer.b\OneDrive - Brighter Futures Learning Partnership Trust\Documents\GitHub\Computer-Science-Programming-Projects\Program\Inventory.txt"
    InventoryScreen = tkinter.Tk


# doesnt work for some reason, having issues with getting the label to run
# needed to make with and height

# fixed issue 

    #UserEntry = 





LoginSystem()    
