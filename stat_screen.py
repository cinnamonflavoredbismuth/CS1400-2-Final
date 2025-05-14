import pygame
import csv
import random
from unit import unit_select
from basic_functions import pystart, clear, if_clicked, display, display_buttons, button #imported from basic_functions.py
from account_handler import leaderboard, load
import time

# Define the Spanish or Vanish game
# This is a simple game where the user selects the correct answer from multiple options.
# The game will display a lesson and multiple options, and the user has to select the correct one.
# The game will be played using Pygame, a popular library for creating games in Python.

def lessons(acc): # Displays the user's streak, the streak leaderboard, and the options to start or quit
    while True:
        
        # Initialize Pygame
        screen = pystart()


        # Image background


        # Set up fonts
        font = pygame.font.Font(None, 36)


        #Set up buttons
        buttons={
        'Quit_btn' : button(500, 50, {"x" :  325,"y" : 630},"Quit", "Arial", 35, (80,80,80), (40,40,40), 225, 0, (255,255,255),False),
        'Start_btn' : button(500, 50, {"x" :  325,"y" : 530},"Start", "Arial", 35, (80,80,80), (40,40,40), 215, 0, (255,255,255),False),

        'Board' : button(325, 325, {"x" :  425,"y" : 125},"", "Arial", 35, (80,80,80), (80,80,80), 200, 0, (255,255,255),False)}

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

            # Displays user's streak
            surface = font.render(f"{acc.name}'s Streak: {acc.streak}", True, (0, 0, 0))
            screen.blit(surface, (450, 50))

            # Displays Streak Leaderboard
            surface = font.render("Streak Leaderboard:", True, (0, 0, 0))
            screen.blit(surface, (450, 150))
            ranked_streaks = leaderboard()
            for rank, streak in enumerate(ranked_streaks[:5]):
                surface = font.render(f"{rank+1}. {streak[1]} - {streak[0]} days", True, (0, 0, 0))
                screen.blit(surface, (450, 200 + (rank*50)))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if if_clicked(buttons['Quit_btn'],event) == True: # If  quit button clicked
                        # Go back to the main menu
                        running = False

                    elif if_clicked(buttons['Start_btn'],event) == True: # If Start button 
                        time.sleep(0.5)
                        unit_select(acc)

            pygame.display.flip()  # Update the display
            pygame.time.delay(100)  # Delay to control frame rate

        # End of the game loop

        display("Returning to Main Menu!", 2)
        break
acc=load('cecily')
#lessons(acc)