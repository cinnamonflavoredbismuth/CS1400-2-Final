import pygame
import csv
import random
import time
from basic_functions import pystart, clear, display_buttons, if_clicked, display, wrong_sound, button
from lesson import lesson


# Define the Spanish or Vanish game
# This is a simple game where the user selects the correct answer from multiple options.
# The game will display a lesson and multiple options, and the user has to select the correct one.
# The game will be played using Pygame, a popular library for creating games in Python.

def lesson_select(unit, acc): # Lets the user pick which lesson they want to do
    time.sleep(0.5)

    # Initialize Pygame
    pystart()

    def lesson_btn(coords,num,status):
        return button(500, 50, coords,f"Lesson {num}", "Arial", 35, (80,80,80), (40,40,40), 175, 0, (255,255,255),status)
    #Set up buttons
    buttons={
    'lesson_1_btn' : lesson_btn({"x" :  50,"y" : 200},1,False),
    'lesson_2_btn' : lesson_btn({"x" :  50,"y" : 300}, 2,False),
    'lesson_3_btn': lesson_btn({"x" :  50,"y" : 400},3,False),
    'lesson_4_btn' : lesson_btn({"x" :  50,"y" : 500},4,False),
    'lesson_5_btn' : lesson_btn({"x" :  650,"y" : 200},5,False),
    'lesson_6_btn' : lesson_btn({"x" :  650,"y" : 300},6,False),
    'lesson_7_btn' : lesson_btn({"x" :  650,"y" : 400},7,False),
    'quiz_btn' : button(500, 50, {"x" :  650,"y" : 500},"Quiz", "Arial", 35, (80,80,80), (40,40,40), 175, 0, (255,255,255),False),
    'return_btn' : button(500, 50, {"x" :  350,"y" : 600},"Return", "Arial", 35, (80,80,80), (40,40,40), 225, 0, (255,255,255),False)
}


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
                if if_clicked(buttons['lesson_1_btn'],event) == True: # If  quit button clicked
                    # Go back to the main menu
                    if int(acc.lesson) >= 1:
                        _lesson = ' 1'
                        
                        lesson(unit, _lesson, [], [],acc)
                        running = False
                    else:
                        wrong_sound()
                        pass

                elif if_clicked(buttons['lesson_2_btn'],event) == True:
                    if int(acc.lesson) >= 2:
                        _lesson = ' 2'
                        
                        lesson(unit, _lesson, [], [],acc)
                        running = False
                    else:
                        wrong_sound()
                        pass
                elif if_clicked(buttons['lesson_3_btn'],event) == True:
                    if int(acc.lesson) >= 3:
                        _lesson = ' 3'
                        
                        lesson(unit, _lesson, [], [],acc)
                        running = False
                    else:
                        wrong_sound()
                        pass
                elif if_clicked(buttons['lesson_4_btn'],event) == True:
                    if int(acc.lesson) >= 4:
                        _lesson = ' 4'
                        
                        lesson(unit, _lesson, [], [],acc)
                        running = False
                    else:
                        wrong_sound()
                        pass
                elif if_clicked(buttons['lesson_5_btn'],event) == True:
                    if int(acc.lesson) >= 5:
                        _lesson = ' 5'
                        
                        lesson(unit, _lesson, [], [],acc)
                        running = False
                    else:
                        wrong_sound()
                        pass
                elif if_clicked(buttons['lesson_6_btn'],event) == True:
                    if int(acc.lesson) >= 6:
                        _lesson = ' 6'
                        
                        lesson(unit, _lesson, [], [],acc)
                        running = False
                    else:
                        wrong_sound()
                        pass
                elif if_clicked(buttons['lesson_7_btn'],event) == True:
                    if int(acc.lesson) >= 7:
                        _lesson = ' 7'
                        
                        lesson(unit, _lesson, [], [],acc)
                        running = False
                    else:
                        wrong_sound()
                        pass
                elif if_clicked(buttons['quiz_btn'],event) == True:
                    if int(acc.lesson) >= 8:
                        _lesson = 'quiz'
        
                        lesson(unit, _lesson, [], [],acc)
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
    display("Returning to Unit Select Page!", 2)
