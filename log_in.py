# Log In -Luke Murdock
from basic_functions import display, txt_input
from account_handler import log_in, load
from spanish import lessons

def get_log_in():
    display('Username: ',0,x=0,y=0)
    name = txt_input(50,50).strip()
    display('Password: ',0,x=0,y=0)
    password = txt_input(50,50).strip()

    if log_in(name, password) == True:
        display(f'You have logged in as {name}!',2)
        acc = load(name)
        lessons(acc)
    else:
        display('Username or password could not be found',4)