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
        name=(txt_input("Username: ",x=50,y=50).strip())
        print(name)
        clear()
        password=(txt_input("Password: ",x=50,y=50).strip())
        acc=new(name,password)
        clear()
        if acc == False:
            display("Account already exists", 3,x=100,y=100)
            return False
        else: 
            display("Account created", 3,x=100,y=100)
            return name
#new_account()
#new_account()

# Log In -Luke Murdock

def get_log_in(): # Lets the user input their name amd password to find if their account exists and then tells them the result
    pystart()
    running = True
    while running:
        clear()
        display('Username: ',0,x=0,y=0)
        name=(txt_input("Username: ",x=50,y=50).strip())
        password=(txt_input("Password: ",x=50,y=50).strip())

        if log_in(name, password) == True:
            clear()
            display(f'You have logged in as {name}!',2,100)
            return name
        else:
            clear()
            display('Username or password could not be found',2,100)
            return False