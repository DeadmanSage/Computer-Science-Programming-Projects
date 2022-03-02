import tkinter
from tkinter import *
import tkinter.font as font
import tkinter.messagebox
LoginScreen = None
BackColour = "#b3b1b1"
#def messageCall():
#    tkinter.messagebox.showinfo("hello world", "hello world")
#screen = tkinter.Tk()
#myfont = font.Font(family = 'american typewriter') #creates a font variable to be used
#screen.geometry("250x250") #window size
#screen.title("window title") #window title
#b = tkinter.Button(screen, text="Click here", font = myfont, bd = 7, fg = 'blue', activeforeground = 'red', height = 2, command = messageCall) #creates a button variable
#b.place(relx = 0.5, rely = 0.5, anchor = CENTER) #places the button variable
#screen.mainloop() #required to start instructions

def MainScreen():
    main_screen = Tk()
    

def LoginSystem():
    global LoginScreen
    file = open("Login.txt")
    LoginScreen = tkinter.Tk()
    LoginScreen.config(bg=BackColour)
    LoginScreen.title("Sign into Account")
    LoginScreen.geometry("500x500")
    #makes a screen for login
    Label(text="Login with school account to continue", bg="white", width="30",height="1", font=("Calibri", 10)).place(relx=0.3,rely=0.5, anchor=CENTER)
    
    Button(text="Login", height=2, width=20).place(relx=0.3,rely=0.8, anchor=CENTER)

# doesnt work for some reason, having issues with getting the label to run
# needed to make with and height

    #UserEntry = 



LoginSystem()

LoginScreen.mainloop()