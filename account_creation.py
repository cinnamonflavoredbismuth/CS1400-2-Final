#Spanish or Vanish Account Creation screen
import pygame
from account_handler import new_account as new
from basic_functions import txt_input, display
def new_account():
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Spanish or Vanish')
    pygame.display.set_icon(pygame.image.load('logo_uwu.png'))


    # Image background
    background_image = pygame.image.load('BG.webp')  # Load the image
    background_image = pygame.transform.scale(background_image, (1200, 800))  # Scale to fit the screen
    running = True
    while running:
        screen.fill((255, 255, 255))  # Clear the screen with a white background
        screen.blit(background_image, (0,0)) #Display the background
        # find the x and y for acc creation
        display("Name:", 3)
        print
        name=(txt_input(0,0))
        print(name)
        screen.blit(background_image, (0,0)) #Display the background
        display("Password", 3)
        password=(txt_input(0,0))
        acc=new(name,password)
        if acc == False:
            display("Account already exists", 3)
        else: 
            display("Account created", 3)
new_account()