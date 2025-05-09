import pygame
import csv
import random
from basic_functions import btn
from lesson_select import lesson_select
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
        return_btn = {
        "width" : 250, # width of the button
        "height" : 50, # height of the button
        "StartPos": {"x" :  10,"y" : 730}, # Top left is 0,0
        "text": "Return", 
        "font": "Arial",
        "fontsize": 35,
        "hover_color": (80,80,80),
        "main_color": (40,40,40),
        "text_offset": 75,
        "verticle_text_offset": 0,
        "text_color": (255,255,255)
        }

        



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
                    if unit1_btn['StartPos']['x'] <= event.pos[0] <= unit1_btn['StartPos']['x'] + unit1_btn['width'] and unit1_btn['StartPos']['y'] <= event.pos[1] <= unit1_btn['StartPos']['y'] + unit1_btn['height']:
                        # Go back to the main menu
                        unit = 'Basics'
                        click()
                        lesson_select(unit)
                        running = False

                    elif unit2_btn['StartPos']['x'] <= event.pos[0] <= unit2_btn['StartPos']['x'] + unit2_btn['width'] and unit2_btn['StartPos']['y'] <= event.pos[1] <= unit2_btn['StartPos']['y'] + unit2_btn['height']:
                        unit = 'Directions'
                        click()
                        lesson_select(unit)
                        running = False

                    elif unit3_btn['StartPos']['x'] <= event.pos[0] <= unit3_btn['StartPos']['x'] + unit3_btn['width'] and unit3_btn['StartPos']['y'] <= event.pos[1] <= unit3_btn['StartPos']['y'] + unit3_btn['height']:
                        unit = 'Small Talk'
                        click()
                        lesson_select(unit)
                        running = False
                    
                    elif unit4_btn['StartPos']['x'] <= event.pos[0] <= unit4_btn['StartPos']['x'] + unit4_btn['width'] and unit4_btn['StartPos']['y'] <= event.pos[1] <= unit4_btn['StartPos']['y'] + unit4_btn['height']:
                        unit = 'Food'
                        click()
                        lesson_select(unit)
                        running = False

                    elif return_btn['StartPos']['x'] <= event.pos[0] <= return_btn['StartPos']['x'] + return_btn['width'] and return_btn['StartPos']['y'] <= event.pos[1] <= return_btn['StartPos']['y'] + return_btn['height']:
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
