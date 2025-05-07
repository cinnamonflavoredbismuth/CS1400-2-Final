# Log In -Luke Murdock
from basic_functions import txt_input, display
from account_handler import log_in, load
from spanish import lessons

def get_log_in():
    # name = txt_input('Username: ').strip()
    # password = txt_input('Password: ').strip()
    name = "luke.murdock"
    password = "123"

    if log_in(name, password) == True:
        display(f'You have logged in as {name}!',3)
        acc = load(name)
        # lessons(acc)
        lessons()
    else:
        display('Username or password could not be found',4)