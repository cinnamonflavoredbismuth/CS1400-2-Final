import pygame
import csv
import random
from basic_functions import pystart, display_buttons, display, wrong_sound
from lesson_select import lesson_select, if_clicked, clear, button

# Define the Spanish or Vanish game
# This is a simple game where the user selects the correct answer from multiple options.
# The game will display a lesson and multiple options, and the user has to select the correct one.
# The game will be played using Pygame, a popular library for creating games in Python.

def unit_select(acc): # Lets the user pick which unit they want to do
    while True:
        # Initialize Pygame
        pystart()
        #Set up buttons
        buttons={'unit1_btn' : button(500,50,{"x" :  325,"y" : 130},"Unit 1", "Arial", 35, (80,80,80), (40,40,40), 215, 0, (255,255,255),False),
        'unit2_btn' : button(500,50,{"x" :  325,"y" : 230},"Unit 2", "Arial", 35, (80,80,80), (40,40,40), 215, 0, (255,255,255),False),
        'unit3_btn' : button(500,50,{"x" :  325,"y" : 330},"Unit 3", "Arial", 35, (80,80,80), (40,40,40), 215, 0, (255,255,255),False),
        'unit4_btn' : button(500,50,{"x" :  325,"y" : 430},"Unit 4", "Arial", 35, (80,80,80), (40,40,40), 215, 0, (255,255,255),False),
        'return_btn' : button(250, 50, {"x" :  10,"y" : 730},"Return", "Arial",35,(80,80,80),(40,40,40),75,0,(255,255,255),False)}

        # Load lessons and questions from CSV
        lessons = []
        with open('csv_files/Lessons.csv', 'r') as file:
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
                        unit = 'Basics'
                        lesson_select(unit, acc)

                    elif if_clicked(buttons['unit2_btn'],event) == True:
                        unit = 'Directions'
                        lesson_select(unit, acc)

                    elif if_clicked(buttons['unit3_btn'],event) == True:
                        unit = 'Small Talk'
                        lesson_select(unit, acc)
                    
                    elif if_clicked(buttons['unit4_btn'],event) == True:
                        unit = 'Food'
                        lesson_select(unit, acc)

                    elif if_clicked(buttons['return_btn'],event) == True:
                        running = False
                    
                elif if_clicked(buttons['unit4_btn'],event) == True:
                    if int(acc.unit) == 4:
                        unit = 'Food'
                        lesson_select(unit, acc)
                    else:
                        wrong_sound()
                        pass

                elif if_clicked(buttons['return_btn'],event) == True:
                    # Go back to the main menu
                    
                    running = False
                

            

            pygame.display.flip()  # Update the display
            pygame.time.delay(100)  # Delay to control frame rate

        # End of the game loop
        display("Returning to Stat Page!", 2)
        break

'''acc=load('cecily')
unit_select(acc)'''
