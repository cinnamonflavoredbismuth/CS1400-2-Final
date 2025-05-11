import pygame
import csv
import random
from spanish import lessons
from basic_functions import btn, display, click, start_up, bgm, if_clicked, clear, button, pystart
from log_in import get_log_in
from account_creation import new_account
from account_handler import load

# Define the Spanish or Vanish game
# This is a simple game where the user selects the correct answer from multiple options.
# The game will display a lesson and multiple options, and the user has to select the correct one.
# The game will be played using Pygame, a popular library for creating games in Python.

screen = pystart()

# Image background
bird1 = pygame.image.load("logo_uwu.png")
bird2 = pygame.transform.flip(bird1, True, False)  # Flip the image horizontally
bird1 = pygame.transform.scale(bird1, (200, 200))  # Scale the image to fit the screen 
bird2 = pygame.transform.scale(bird2, (200, 200))  # Scale the image to fit the screen

# Set up fonts
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 72)  # Larger font for the title

# Render the title
title_text = title_font.render('Spanish or Vanish', True, (0, 0, 0))  # White color

# Position the title at the top center of the screen
title_rect = title_text.get_rect(center=(600, 50))  # Centered at the top of the screen

#Set up buttons
Quit_btn = button(500, 50, {"x" :  325,"y" : 630},"Quit", "Arial", 35, (80,80,80), (40,40,40), 225, 0, (255,255,255))
Account_create_btn = button(500, 50, {"x" :  325,"y" : 530},"Create Account", "Arial", 35, (80,80,80), (40,40,40), 150, 0, (255,255,255))
Log_in_btn = button(500, 50, {"x" :  325,"y" : 430},"Log In", "Arial", 35, (80,80,80), (40,40,40), 200, 0, (255,255,255))

# Main loop
def main_menu():
    bgm()
    while True:
        running = True
        while running:
            clear()
            # Display the options
            btn(Quit_btn)
            btn(Account_create_btn)
            btn(Log_in_btn)
            screen.blit(bird1, (30, 0)) # Draw the first bird image at (0, 0)
            screen.blit(bird2, (900,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if if_clicked(Quit_btn,event) == True: # If  quit button clicked
                        # Go back to the main menu
                        click()
                        running = False

                    elif if_clicked(Account_create_btn,event) == True: # If Account Create button clicked
                        click()
                        name=new_account()
                        if name == None:
                            main_menu()
                        else:
                            acc=load(name)
                            lessons(acc)

                        

                    elif if_clicked(Log_in_btn,event) == True: # If Log In button clicked
                        lessons()

            pygame.display.flip()  # Update the display
            pygame.time.delay(100)  # Delay to control frame rate


        #display("Thank you for playing!",3)
        pygame.quit()
        break


start_up()


main_menu()
