#Spanish or Vanish Account Creation screen
import pygame
from account_handler import new_account as new, log_in
from basic_functions import txt_input, display,clear, pystart

def new_account(): # 
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

def get_log_in(): # 
    display('Username: ',0,x=0,y=0)
    name = txt_input(50,50).strip()
    display('Password: ',0,x=0,y=0)
    password = txt_input(50,50).strip()

    if log_in(name, password) == True:
        display(f'You have logged in as {name}!',2)
        return name
    else:
        display('Username or password could not be found',4)