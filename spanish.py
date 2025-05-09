import pygame
import csv
import random
from unit import unit_select
<<<<<<< HEAD
from basic_functions import *

=======
from basic_functions import btn, display
from basic_functions import click
from misc import display_streaks
>>>>>>> c33cff1d01d89f7dc731f86ef46874d6a179c1d0
# Define the Spanish or Vanish game
# This is a simple game where the user selects the correct answer from multiple options.
# The game will display a lesson and multiple options, and the user has to select the correct one.
# The game will be played using Pygame, a popular library for creating games in Python.
def lessons(acc):
    while True:
        
        # Initialize Pygame
<<<<<<< HEAD
        pystart()
=======
        pygame.init()

        # Set up the display
        screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Spanish or Vanish')
        pygame.display.set_icon(pygame.image.load('logo_uwu.png'))
        #pygame.display.set_caption('Spanish or Vanish')
>>>>>>> c33cff1d01d89f7dc731f86ef46874d6a179c1d0


        # Image background
        background_image = pygame.image.load('BG.webp')  # Load the image
        background_image = pygame.transform.scale(background_image, (1200, 800))  # Scale to fit the screen

        # Set up fonts
        font = pygame.font.Font(None, 36)
        title_font = pygame.font.Font(None, 72)  # Larger font for the title

        #Set up buttons
        Quit_btn = button(500, 50, {"x" :  325,"y" : 630},"Quit", "Arial", 35, (80,80,80), (40,40,40), 225, 0, (255,255,255))
        Start_btn = button(500, 50, {"x" :  325,"y" : 530},"Start", "Arial", 35, (80,80,80), (40,40,40), 215, 0, (255,255,255))



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
            btn(Quit_btn)
            btn(Start_btn)
            # display_streaks(acc)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
<<<<<<< HEAD
                    if if_clicked(Quit_btn,event) == True: # If  quit button clicked
                        # Go back to the main menu
                        running = False

                    elif if_clicked(Start_btn,event) == True: # If Start button clicked
=======
                    if Quit_btn['StartPos']['x'] <= event.pos[0] <= Quit_btn['StartPos']['x'] + Quit_btn['width'] and Quit_btn['StartPos']['y'] <= event.pos[1] <= Quit_btn['StartPos']['y'] + Quit_btn['height']:
                        click()
                        # Go back to the main menu
                        running = False

                    elif Start_btn['StartPos']['x'] <= event.pos[0] <= Start_btn['StartPos']['x'] + Start_btn['width'] and Start_btn['StartPos']['y'] <= event.pos[1] <= Start_btn['StartPos']['y'] + Start_btn['height']:
                        click()
>>>>>>> c33cff1d01d89f7dc731f86ef46874d6a179c1d0
                        unit_select()

                    
                    

            

            pygame.display.flip()  # Update the display
            pygame.time.delay(100)  # Delay to control frame rate

        # End of the game loop
<<<<<<< HEAD
        final_message = "Returning to Main Menu!"
        final_surface = font.render(final_message, True, (0, 0, 0))
        clear()
        screen.blit(final_surface, (50, 50))
        pygame.display.flip()  # Update the display
        pygame.time.delay(2000)  # Wait for 2 seconds before quitting
=======
        display("Returning to Main Menu!",2)
>>>>>>> c33cff1d01d89f7dc731f86ef46874d6a179c1d0
        break
