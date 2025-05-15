#Spanish or Vanish Account Creation screen
import pygame
from account_handler import new_account as new, log_in
from basic_functions import txt_input, display,clear, pystart

def new_account(): # Lets the user input their name amd password for their new account and then tells them if it was created
    pystart()
    running = True
    while running:
        clear()
        # find the x and y for acc creation
        display("Name:", 0,x=0,y=0)
        name=(txt_input(0,20))
        print(name)
        clear()
        display("Password", 0,x=0,y=0)
        password=(txt_input(0,20))
        acc=new(name,password)
        if acc == False:
            display("Account already exists", 3,x=0,y=0)
            return None
        else: 
            display("Account created", 3,x=0,y=0)
            return name
#new_account()


# Log In -Luke Murdock

def get_log_in(): # Lets the user input their name amd password to find if their account exists and then tells them the result
    pystart()
    running = True
    while running:
        clear()
        display('Username: ',0,x=0,y=0)
        name = (txt_input(20,50).strip())
        display('Password: ',0,x=0,y=0)
        password = txt_input(0,20).strip()

        if log_in(name, password) == True:
            display(f'You have logged in as {name}!',2)
            return name
        else:
            display('Username or password could not be found',4)