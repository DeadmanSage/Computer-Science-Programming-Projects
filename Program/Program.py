
import tkinter
from tkinter import *
import tkinter.font as font
import tkinter.messagebox
LoginScreen = None
BackColour = "#b3b1b1" # set the bakcground colour as a variable since it will be easier to call and make programming faster

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
def MainScreen():
    main_screen = tkinter.Tk()
    LoginSystem()

def LoginSystem():
    file = open("Login.txt")

    LoginScreen = TopLevel(main_screen)
    LoginScreen.config(bg=BackColour) # setting the background colour
    LoginScreen.title("Sign into Account") # window title
    LoginScreen.geometry("500x500") # window size
    #makes a screen for login

    username_check = StringVar()
    password_check = StringVar()

    #Label(LoginScreen, text="Login with school account to continue", bg="white", width="30",height="1", font=("Calibri", 10)).place(relx=0.3,rely=0.5, anchor=CENTER)
    #Label(LoginScreen, text="Username ").pack()
    #username_entry = Entry(LoginScreen, textvariable=username_check)
    #username_entry.pack()
    #Label(LoginScreen, text="").pack()

    Button(text="Login", height=2, width=20).place(relx=0.3,rely=0.8, anchor=CENTER)


# doesnt work for some reason, having issues with getting the label to run
# needed to make with and height

# fixed issue 

    #UserEntry = 



#function = LoginSystem()


MainScreen()
main_screen.mainloop()
    