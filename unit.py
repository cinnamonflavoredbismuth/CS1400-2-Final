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
        pystart()
        #Set up buttons
        buttons={'unit1_btn' : button(500,50,{"x" :  325,"y" : 330},"Unit 1", "Arial", 35, (80,80,80), (40,40,40), 215, 0, (255,255,255)),
        'unit2_btn' : button(500,50,{"x" :  325,"y" : 430},"Unit 2", "Arial", 35, (80,80,80), (40,40,40), 215, 0, (255,255,255)),
        'unit3_btn' : button(500,50,{"x" :  325,"y" : 530},"Unit 3", "Arial", 35, (80,80,80), (40,40,40), 215, 0, (255,255,255)),
        'unit4_btn' : button(500,50,{"x" :  325,"y" : 630},"Unit 4", "Arial", 35, (80,80,80), (40,40,40), 215, 0, (255,255,255)),
        'return_btn' : button(250, 50, {"x" :  10,"y" : 730},"Return", "Arial",35,(80,80,80),(40,40,40),75,0,(255,255,255))}

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
            clear()
            # Display the options
            display_buttons(buttons)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if if_clicked(buttons['unit1_btn'],event) == True:
                        # Go back to the main menu
                        unit = 'Basics'
                        
                        lesson_select(unit)
                        running = False

                    elif if_clicked(buttons['unit2_btn'],event) == True:
                        unit = 'Directions'
                        
                        lesson_select(unit)
                        running = False

                    elif if_clicked(buttons['unit3_btn'],event) == True:
                        unit = 'Small Talk'
                        
                        lesson_select(unit)
                        running = False
                    
                    elif if_clicked(buttons['unit4_btn'],event) == True:
                        unit = 'Food'
                        
                        lesson_select(unit)
                        running = False

                    elif if_clicked(buttons['return_btn'],event) == True:
                        # Go back to the main menu
                        
                        running = False
                    

            

            pygame.display.flip()  # Update the display
            pygame.time.delay(100)  # Delay to control frame rate

        # End of the game loop
        final_message = "Returning to Stat Page!"
        final_surface(final_message)
        break


