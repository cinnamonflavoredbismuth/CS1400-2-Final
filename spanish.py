import pygame
import csv
import random
from unit import unit_select
from basic_functions import btn

# Define the Spanish or Vanish game
# This is a simple game where the user selects the correct answer from multiple options.
# The game will display a lesson and multiple options, and the user has to select the correct one.
# The game will be played using Pygame, a popular library for creating games in Python.
def lessons():
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
        Quit_btn = {
        "width" : 500, # width of the button
        "height" : 50, # height of the button
        "StartPos": {"x" :  325,"y" : 630}, # Top left is 0,0
        "text": "Quit", 
        "font": "Arial",
        "fontsize": 35,
        "hover_color": (80,80,80),
        "main_color": (40,40,40),
        "text_offset": 225,
        "text_color": (255,255,255)
        }
        Start_btn = {
        "width" : 500, # width of the button
        "height" : 50, # height of the button
        "StartPos": {"x" :  325,"y" : 530}, # Top left is 0,0
        "text": "Start", 
        "font": "Arial",
        "fontsize": 35,
        "hover_color": (80,80,80),
        "main_color": (40,40,40),
        "text_offset": 215,
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
            btn(Quit_btn)
            btn(Start_btn)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if Quit_btn['StartPos']['x'] <= event.pos[0] <= Quit_btn['StartPos']['x'] + Quit_btn['width'] and Quit_btn['StartPos']['y'] <= event.pos[1] <= Quit_btn['StartPos']['y'] + Quit_btn['height']:
                        # Go back to the main menu
                        running = False

                    elif Start_btn['StartPos']['x'] <= event.pos[0] <= Start_btn['StartPos']['x'] + Start_btn['width'] and Start_btn['StartPos']['y'] <= event.pos[1] <= Start_btn['StartPos']['y'] + Start_btn['height']:
                        unit_select()

                    
                    

            

            pygame.display.flip()  # Update the display
            pygame.time.delay(100)  # Delay to control frame rate

        # End of the game loop
        final_message = "Returning to Stat page!"
        final_surface = font.render(final_message, True, (0, 0, 0))
        screen.fill((255, 255, 255))  # Clear the screen for the final message
        screen.blit(background_image, (0,0))
        screen.blit(final_surface, (50, 50))
        pygame.display.flip()  # Update the display
        pygame.time.delay(2000)  # Wait for 2 seconds before quitting
        break
