# Log In -Luke Murdock
from basic_functions import txt_input, display
from account_handler import log_in, load

def get_log_in():
    name = txt_input('\nUsername: ').strip()
    password = txt_input('Password: ').strip()

    if log_in(name, password) == True:
        display(f'\nYou have logged in as {name}!',3)
        acc = load(name)
        menu(acc)
    else:
        display(f'\nUsername or password could not be found',4)