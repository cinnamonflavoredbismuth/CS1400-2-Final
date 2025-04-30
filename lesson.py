import pygame
import csv
import random
from basic_functions import btn
# from sign_up_screen import * 

# Define the Spanish or Vanish game
# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Spanish or Vanish')
pygame.display.set_icon(pygame.image.load('logo_uwu.png'))


# Image background
background_image = pygame.image.load('BG.webp')  # Load the image
background_image = pygame.transform.scale(background_image, (1200, 800))  # Scale to fit the screen
bird1 = pygame.image.load("logo_uwu.png")
bird2 = pygame.image.load("logo_uwu.png")
bird2 = pygame.transform.flip(bird2, True, False)  # Flip the image horizontally
bird1 = pygame.transform.scale(bird1, (200, 200))  # Scale the image to fit the screen 
bird2 = pygame.transform.scale(bird2, (200, 200))  # Scale the image to fit the screen

#Create Button date
option1_btn = {
        "width" : 300, # width of the button
        "height" : 150, # height of the button
        "StartPos": {"x" :  250,"y" : 330}, # Top left is 0,0
        "text": "Answer 1", 
        "font": "Arial",
        "fontsize": 35,
        "hover_color": (200,200,200),
        "main_color": (255,255,255),
        "text_offset": 75,
        "verticle_text_offset": 60,
        "text_color": (50,50,50)
        }
option2_btn = {
        "width" : 300, # width of the button
        "height" : 150, # height of the button
        "StartPos": {"x" :  650,"y" : 330}, # Top left is 0,0
        "text": "Answer 2", 
        "font": "Arial",
        "fontsize": 35,
        "hover_color": (200,200,200),
        "main_color": (255,255,255),
        "text_offset": 75,
        "verticle_text_offset": 60,
        "text_color": (50,50,50)
        }
option3_btn = {
        "width" : 300, # width of the button
        "height" : 150, # height of the button
        "StartPos": {"x" :  250,"y" : 530}, # Top left is 0,0
        "text": "Answer 3", 
        "font": "Arial",
        "fontsize": 35,
        "hover_color": (200,200,200),
        "main_color": (255,255,255),
        "text_offset": 75,
        "verticle_text_offset": 60,
        "text_color": (50,50,50)
        }
option4_btn = {
        "width" : 300, # width of the button
        "height" : 150, # height of the button
        "StartPos": {"x" :  650,"y" : 530}, # Top left is 0,0
        "text": "Answer 4", 
        "font": "Arial",
        "fontsize": 35,
        "hover_color": (200,200,200),
        "main_color": (255,255,255),
        "text_offset": 75,
        "verticle_text_offset": 60,
        "text_color": (50,50,50)
        }
quit_btn = {
        "width" : 250, # width of the button
        "height" : 50, # height of the button
        "StartPos": {"x" :  10,"y" : 730}, # Top left is 0,0
        "text": "Quit", 
        "font": "Arial",
        "fontsize": 35,
        "hover_color": (200,200,200),
        "main_color": (255,255,255),
        "text_offset": 90,
        "verticle_text_offset": 0,
        "text_color": (50,50,50)
        }
# Set up fonts
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 72)  # Larger font for the title
def lessons():
    question_text = title_font.render('What is yes in spanish', True, (0, 0, 0))  # White color

    # Position the title at the top center of the screen
    question_rect = question_text.get_rect(center=(600, 100))  # Centered at the top of the screen

    while True:
        running = True
        while running:
            screen.fill((255, 255, 255))  # Clear the screen with a white background
            screen.blit(background_image, (0,0))
            screen.blit(question_text, question_rect)

            btn(option1_btn)
            btn(option2_btn)
            btn(option3_btn)
            btn(option4_btn)
            btn(quit_btn)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if option1_btn['StartPos']['x'] <= event.pos[0] <= option1_btn['StartPos']['x'] + option1_btn['width'] and option1_btn['StartPos']['y'] <= event.pos[1] <= option1_btn['StartPos']['y'] + option1_btn['height']:
                        # Go back to the main menu
                        running = False

                    elif option2_btn['StartPos']['x'] <= event.pos[0] <= option2_btn['StartPos']['x'] + option2_btn['width'] and option2_btn['StartPos']['y'] <= event.pos[1] <= option2_btn['StartPos']['y'] + option2_btn['height']:
                        running = False

                    elif option3_btn['StartPos']['x'] <= event.pos[0] <= option3_btn['StartPos']['x'] + option3_btn['width'] and option3_btn['StartPos']['y'] <= event.pos[1] <= option3_btn['StartPos']['y'] + option3_btn['height']:
                        running = False
                    
                    elif option4_btn['StartPos']['x'] <= event.pos[0] <= option4_btn['StartPos']['x'] + option4_btn['width'] and option4_btn['StartPos']['y'] <= event.pos[1] <= option4_btn['StartPos']['y'] + option4_btn['height']:
                        running = False

                    elif quit_btn['StartPos']['x'] <= event.pos[0] <= quit_btn['StartPos']['x'] + quit_btn['width'] and quit_btn['StartPos']['y'] <= event.pos[1] <= quit_btn['StartPos']['y'] + quit_btn['height']:
                        # Go back to the main menu
                        running = False

                    
    
            pygame.display.flip()  # Update the display
            pygame.time.delay(100)  # Delay to control frame rat

        # End of the game loop
        final_message = "Thank you for playing!"
        final_surface = font.render(final_message, True, (0, 0, 0))
        screen.fill((255, 255, 255))  # Clear the screen for the final message
        screen.blit(background_image, (0,0))
        screen.blit(final_surface, (50, 50))
        pygame.display.flip()  # Update the display
        pygame.time.delay(2000)  # Wait for 2 seconds before quitting
        # Quit Pygame
        
lessons()