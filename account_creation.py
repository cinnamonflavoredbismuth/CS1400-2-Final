#Spanish or Vanish Account Creation screen
import pygame
from account_handler import new_account as new
from basic_functions import txt_input, display,clear, pystart
def new_account():
    '''  pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Spanish or Vanish')
    pygame.display.set_icon(pygame.image.load('logo_uwu.png'))'''
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