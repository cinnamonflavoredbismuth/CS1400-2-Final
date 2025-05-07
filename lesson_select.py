import pygame
import csv
import random
from basic_functions import btn
from lesson import lesson

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
    lesson_1_btn = {
    "width" : 500, # width of the button
    "height" : 50, # height of the button
    "StartPos": {"x" :  50,"y" : 200}, # Top left is 0,0
    "text": "Lesson 1", 
    "font": "Arial",
    "fontsize": 35,
    "hover_color": (80,80,80),
    "main_color": (40,40,40),
    "text_offset": 175,
    "verticle_text_offset": 0,
    "text_color": (255,255,255)
    }
    lesson_2_btn = {
    "width" : 500, # width of the button
    "height" : 50, # height of the button
    "StartPos": {"x" :  50,"y" : 300}, # Top left is 0,0
    "text": "Lesson 2", 
    "font": "Arial",
    "fontsize": 35,
    "hover_color": (80,80,80),
    "main_color": (40,40,40),
    "text_offset": 175,
    "verticle_text_offset": 0,
    "text_color": (255,255,255)
    }
    lesson_3_btn = {
    "width" : 500, # width of the button
    "height" : 50, # height of the button
    "StartPos": {"x" :  50,"y" : 400}, # Top left is 0,0
    "text": "Lesson 3", 
    "font": "Arial",
    "fontsize": 35,
    "hover_color": (80,80,80),
    "main_color": (40,40,40),
    "text_offset": 175,
    "verticle_text_offset": 0,
    "text_color": (255,255,255)
    }
    lesson_4_btn = {
    "width" : 500, # width of the button
    "height" : 50, # height of the button
    "StartPos": {"x" :  50,"y" : 500}, # Top left is 0,0
    "text": "Lesson 4", 
    "font": "Arial",
    "fontsize": 35,
    "hover_color": (80,80,80),
    "main_color": (40,40,40),
    "text_offset": 175,
    "verticle_text_offset": 0,
    "text_color": (255,255,255)
    }
    lesson_5_btn = {
    "width" : 500, # width of the button
    "height" : 50, # height of the button
    "StartPos": {"x" :  650,"y" : 200}, # Top left is 0,0
    "text": "Lesson 5", 
    "font": "Arial",
    "fontsize": 35,
    "hover_color": (80,80,80),
    "main_color": (40,40,40),
    "text_offset": 175,
    "verticle_text_offset": 0,
    "text_color": (255,255,255)
    }
    lesson_6_btn = {
    "width" : 500, # width of the button
    "height" : 50, # height of the button
    "StartPos": {"x" :  650,"y" : 300}, # Top left is 0,0
    "text": "Lesson 6", 
    "font": "Arial",
    "fontsize": 35,
    "hover_color": (80,80,80),
    "main_color": (40,40,40),
    "text_offset": 175,
    "verticle_text_offset": 0,
    "text_color": (255,255,255)
    }
    lesson_7_btn = {
    "width" : 500, # width of the button
    "height" : 50, # height of the button
    "StartPos": {"x" :  650,"y" : 400}, # Top left is 0,0
    "text": "Lesson 7", 
    "font": "Arial",
    "fontsize": 35,
    "hover_color": (80,80,80),
    "main_color": (40,40,40),
    "text_offset": 175,
    "verticle_text_offset": 0,
    "text_color": (255,255,255)
    }
    return_btn = {
    "width" : 500, # width of the button
    "height" : 50, # height of the button
    "StartPos": {"x" :  650,"y" : 500}, # Top left is 0,0
    "text": "Return", 
    "font": "Arial",
    "fontsize": 35,
    "hover_color": (80,80,80),
    "main_color": (40,40,40),
    "text_offset": 190,
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
        screen.blit(background_image, (0,0)) #Display the background
        # Display the options
        btn(lesson_1_btn)
        btn(lesson_2_btn)
        btn(lesson_3_btn)
        btn(lesson_4_btn)
        btn(lesson_5_btn)
        btn(lesson_6_btn)
        btn(lesson_7_btn)
        btn(return_btn)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if lesson_1_btn['StartPos']['x'] <= event.pos[0] <= lesson_1_btn['StartPos']['x'] + lesson_1_btn['width'] and lesson_1_btn['StartPos']['y'] <= event.pos[1] <= lesson_1_btn['StartPos']['y'] + lesson_1_btn['height']:
                    # Go back to the main menu
                    _lesson = ' 1'
                    lesson(unit, _lesson)
                    running = False

                elif lesson_2_btn['StartPos']['x'] <= event.pos[0] <= lesson_2_btn['StartPos']['x'] + lesson_2_btn['width'] and lesson_2_btn['StartPos']['y'] <= event.pos[1] <= lesson_2_btn['StartPos']['y'] + lesson_2_btn['height']:
                    _lesson = ' 2'
                    lesson(unit, _lesson)
                    running = False

                elif lesson_3_btn['StartPos']['x'] <= event.pos[0] <= lesson_3_btn['StartPos']['x'] + lesson_3_btn['width'] and lesson_3_btn['StartPos']['y'] <= event.pos[1] <= lesson_3_btn['StartPos']['y'] + lesson_3_btn['height']:
                    _lesson = ' 3'
                    lesson(unit, _lesson)
                    running = False
                
                elif lesson_4_btn['StartPos']['x'] <= event.pos[0] <= lesson_4_btn['StartPos']['x'] + lesson_4_btn['width'] and lesson_4_btn['StartPos']['y'] <= event.pos[1] <= lesson_4_btn['StartPos']['y'] + lesson_4_btn['height']:
                    _lesson = ' 4'
                    lesson(unit, _lesson)
                    running = False

                elif lesson_5_btn['StartPos']['x'] <= event.pos[0] <= lesson_5_btn['StartPos']['x'] + lesson_5_btn['width'] and lesson_5_btn['StartPos']['y'] <= event.pos[1] <= lesson_5_btn['StartPos']['y'] + lesson_5_btn['height']:
                    _lesson = ' 5'
                    lesson(unit, _lesson)
                    running = False

                elif lesson_6_btn['StartPos']['x'] <= event.pos[0] <= lesson_6_btn['StartPos']['x'] + lesson_6_btn['width'] and lesson_6_btn['StartPos']['y'] <= event.pos[1] <= lesson_6_btn['StartPos']['y'] + lesson_6_btn['height']:
                    _lesson = ' 6'
                    lesson(unit, _lesson)
                    running = False

                elif lesson_7_btn['StartPos']['x'] <= event.pos[0] <= lesson_7_btn['StartPos']['x'] + lesson_7_btn['width'] and lesson_7_btn['StartPos']['y'] <= event.pos[1] <= lesson_7_btn['StartPos']['y'] + lesson_7_btn['height']:
                    _lesson = ' 7'
                    lesson(unit, _lesson)
                    running = False

                if return_btn['StartPos']['x'] <= event.pos[0] <= return_btn['StartPos']['x'] + return_btn['width'] and return_btn['StartPos']['y'] <= event.pos[1] <= return_btn['StartPos']['y'] + return_btn['height']:
                    # Go back to the main menu
                    running = False
            
                

        

        pygame.display.flip()  # Update the display
        pygame.time.delay(100)  # Delay to control frame rate

    # End of the game loop
    final_message = "Returning to Unit Select Page!"
    final_surface = font.render(final_message, True, (0, 0, 0))
    screen.fill((255, 255, 255))  # Clear the screen for the final message
    screen.blit(background_image, (0,0))
    screen.blit(final_surface, (50, 50))
    pygame.display.flip()  # Update the display
    pygame.time.delay(2000)  # Wait for 2 seconds before quitting
