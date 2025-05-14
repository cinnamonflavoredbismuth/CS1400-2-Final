import pygame
import csv
import random
from basic_functions import birds, pystart, display_buttons, display, wrong_sound
from lesson_select import lesson_select, if_clicked, clear, button, click
import time

# Define the Spanish or Vanish game
# This is a simple game where the user selects the correct answer from multiple options.
# The game will display a lesson and multiple options, and the user has to select the correct one.
# The game will be played using Pygame, a popular library for creating games in Python.
def unit_select(acc):
    while True:
        # Initialize Pygame
        pystart()
        #Set up buttons
        buttons={'unit1_btn' : button(500,50,{"x" :  325,"y" : 330},"Unit 1", "Arial", 35, (80,80,80), (40,40,40), 215, 0, (255,255,255),False),
        'unit2_btn' : button(500,50,{"x" :  325,"y" : 430},"Unit 2", "Arial", 35, (80,80,80), (40,40,40), 215, 0, (255,255,255),False),
        'unit3_btn' : button(500,50,{"x" :  325,"y" : 530},"Unit 3", "Arial", 35, (80,80,80), (40,40,40), 215, 0, (255,255,255),False),
        'unit4_btn' : button(500,50,{"x" :  325,"y" : 630},"Unit 4", "Arial", 35, (80,80,80), (40,40,40), 215, 0, (255,255,255),False),
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
                        # Go back to the main menu
                        unit = 'Basics'
                        time.sleep(0.5)
                        lesson_select(unit, acc)
                        running = False

                elif if_clicked(buttons['unit2_btn'],event) == True:
                    if int(acc.unit) >= 2:
                        unit = 'Directions'
                        time.sleep(0.5)
                        lesson_select(unit, acc)
                        running = False
                    else:
                        wrong_sound()
                        pass

                elif if_clicked(buttons['unit3_btn'],event) == True:
                    if int(acc.unit) >= 3:
                        unit = 'Small Talk'
                        time.sleep(0.5)
                        lesson_select(unit, acc)
                        running = False
                    else:
                        wrong_sound()
                        pass
                    
                elif if_clicked(buttons['unit4_btn'],event) == True:
                    if int(acc.unit) > 4:
                        unit = 'Food'
                        time.sleep(0.5)
                        lesson_select(unit, acc)
                        running = False
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


