import pygame
import csv
import random
from basic_functions import btn
from lesson_select import lesson_select, if_clicked, clear, button, click
from basic_functions import *


# Define the Spanish or Vanish game
# This is a simple game where the user selects the correct answer from multiple options.
# The game will display a lesson and multiple options, and the user has to select the correct one.
# The game will be played using Pygame, a popular library for creating games in Python.
def unit_select():
    while True:
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

        #Set up buttons
        unit1_btn = button(500,50,{"x" :  325,"y" : 330},"Unit 1", "Arial", 35, (80,80,80), (40,40,40), 215, 0, (255,255,255))
        unit2_btn = button(500,50,{"x" :  325,"y" : 430},"Unit 2", "Arial", 35, (80,80,80), (40,40,40), 215, 0, (255,255,255))
        unit3_btn = button(500,50,{"x" :  325,"y" : 530},"Unit 3", "Arial", 35, (80,80,80), (40,40,40), 215, 0, (255,255,255))
        unit4_btn = button(500,50,{"x" :  325,"y" : 630},"Unit 4", "Arial", 35, (80,80,80), (40,40,40), 215, 0, (255,255,255))
        return_btn = button(250, 50, {"x" :  10,"y" : 730},"Return", "Arial",35,(80,80,80),(40,40,40),75,0,(255,255,255))

        



        # Load lessons and questions from CSV
        lessons = []
        with open('Lessons.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                lessons.append(row)

        # Start with the first lesson
        current_lesson = 0
        selected_option = -1  # No option selected initially

        # Define button positions

        # Main loop
        running = True
        while running:
            screen.fill((255, 255, 255))  # Clear the screen with a white background
            screen.blit(background_image, (0,0))
            # Display the options
            btn(unit1_btn)
            btn(unit2_btn)
            btn(unit3_btn)
            btn(unit4_btn)
            btn(return_btn)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if if_clicked(unit1_btn,event) == True:
                        # Go back to the main menu
                        unit = 'Basics'
                        click()
                        lesson_select(unit)
                        running = False

                    elif if_clicked(unit2_btn,event) == True:
                        unit = 'Directions'
                        click()
                        lesson_select(unit)
                        running = False

                    elif if_clicked(unit3_btn,event) == True:
                        unit = 'Small Talk'
                        click()
                        lesson_select(unit)
                        running = False
                    
                    elif if_clicked(unit4_btn,event) == True:
                        unit = 'Food'
                        click()
                        lesson_select(unit)
                        running = False

                    elif if_clicked(return_btn,event) == True:
                        # Go back to the main menu
                        click()
                        running = False
                    

            

            pygame.display.flip()  # Update the display
            pygame.time.delay(100)  # Delay to control frame rate

        # End of the game loop
        final_message = "Returning to Stat Page!"
        final_surface = font.render(final_message, True, (0, 0, 0))
        screen.fill((255, 255, 255))  # Clear the screen for the final message
        screen.blit(background_image, (0,0))
        screen.blit(final_surface, (50, 50))
        pygame.display.flip()  # Update the display
        pygame.time.delay(2000)  # Wait for 2 seconds before quitting
        break


