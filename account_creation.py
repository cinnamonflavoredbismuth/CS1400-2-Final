#Spanish or Vanish Account Creation screen
import pygame
from account_handler import new_account as new
from basic_functions import txt_input
def new_account():
    # Define the Spanish or Vanish game
    # This is a simple game where the user selects the correct answer from multiple options.
    # The game will display a lesson and multiple options, and the user has to select the correct one.
    # The game will be played using Pygame, a popular library for creating games in Python.

    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Spanish or Vanish')
    pygame.display.set_icon(pygame.image.load('logo_uwu.png'))


    # Image background
    background_image = pygame.image.load('BG.webp')  # Load the image
    background_image = pygame.transform.scale(background_image, (1200, 800))  # Scale to fit the screen

    # Set up fonts
    font = pygame.font.Font(None, 36)
    title_font = pygame.font.Font(None, 72)  # Larger font for the title
    running = True
    while running:
        screen.fill((255, 255, 255))  # Clear the screen with a white background
        screen.blit(background_image, (0,0)) #Display the background
        # find the x and y for acc creation
        print(txt_input(0,0))
new_account()