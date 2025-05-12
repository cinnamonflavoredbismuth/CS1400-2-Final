import pygame
import csv
import random
from basic_functions import *
from lesson import lesson
from basic_functions import  button, pystart, clear, if_clicked, btn, display_buttons, final_surface


# Define the Spanish or Vanish game
# This is a simple game where the user selects the correct answer from multiple options.
# The game will display a lesson and multiple options, and the user has to select the correct one.
# The game will be played using Pygame, a popular library for creating games in Python.
def lesson_select(unit):
    # Define the Spanish or Vanish game
    # This is a simple game where the user selects the correct answer from multiple options.
    # The game will display a lesson and multiple options, and the user has to select the correct one.
    # The game will be played using Pygame, a popular library for creating games in Python.

    # Initialize Pygame
    pystart()

    def lesson_btn(coords,num):
        return button(500, 50, coords,f"Lesson {num}", "Arial", 35, (80,80,80), (40,40,40), 175, 0, (255,255,255))
    #Set up buttons
    buttons={
    'lesson_1_btn' : lesson_btn({"x" :  50,"y" : 200},1),
    'lesson_2_btn' : lesson_btn({"x" :  50,"y" : 300}, 2),
    'lesson_3_btn': lesson_btn({"x" :  50,"y" : 400},3),
    'lesson_4_btn' : lesson_btn({"x" :  50,"y" : 500},4),
    'lesson_5_btn' : lesson_btn({"x" :  650,"y" : 200},5),
    'lesson_6_btn' : lesson_btn({"x" :  650,"y" : 300},6),
    'lesson_7_btn' : lesson_btn({"x" :  650,"y" : 400},7),
    'return_btn' : button(500, 50, {"x" :  650,"y" : 500},"Return", "Arial", 35, (80,80,80), (40,40,40), 225, 0, (255,255,255))
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
        clear()
        # Display the options
        display_buttons(buttons)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if if_clicked(buttons['lesson_1_btn'],event) == True: # If  quit button clicked
                    # Go back to the main menu
                    _lesson = ' 1'
                    
                    lesson(unit, _lesson, [], [])
                    running = False

                elif if_clicked(buttons['lesson_2_btn'],event) == True:
                    _lesson = ' 2'
                    
                    lesson(unit, _lesson, [], [])
                    running = False

                elif if_clicked(buttons['lesson_3_btn'],event) == True:
                    _lesson = ' 3'
                    
                    lesson(unit, _lesson, [], [])
                    running = False
                
                elif if_clicked(buttons['lesson_4_btn'],event) == True:
                    _lesson = ' 4'
                    
                    lesson(unit, _lesson, [], [])
                    running = False

                elif if_clicked(buttons['lesson_5_btn'],event) == True:
                    _lesson = ' 5'
                    
                    lesson(unit, _lesson, [], [])
                    running = False

                elif if_clicked(buttons['lesson_6_btn'],event) == True:
                    _lesson = ' 6'
                    
                    lesson(unit, _lesson, [], [])
                    running = False

                elif if_clicked(buttons['lesson_7_btn'],event) == True:
                    _lesson = ' 7'
                    
                    lesson(unit, _lesson, [], [])
                    running = False

                if if_clicked(buttons['return_btn'],event) == True:
                    # Go back to the main menu
                    
                    running = False

        pygame.display.flip()  # Update the display
        pygame.time.delay(100)  # Delay to control frame rate

    # End of the game loop
    final_message = "Returning to Unit Select Page!"
    final_surface(final_message)
