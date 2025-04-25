import pygame
import csv
import random

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
bird1 = pygame.image.load("logo_uwu.png")
bird2 = pygame.image.load("logo_uwu.png")
bird2 = pygame.transform.flip(bird2, True, False)  # Flip the image horizontally
bird1 = pygame.transform.scale(bird1, (200, 200))  # Scale the image to fit the screen 
bird2 = pygame.transform.scale(bird2, (200, 200))  # Scale the image to fit the screen

# Set up fonts
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 72)  # Larger font for the title

# Render the title
title_text = title_font.render('Spanish or Vanish', True, (0, 0, 0))  # White color

# Position the title at the top center of the screen
title_rect = title_text.get_rect(center=(600, 50))  # Centered at the top of the screen

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
Account_create_btn = {
"width" : 500, # width of the button
"height" : 50, # height of the button
"StartPos": {"x" :  325,"y" : 530}, # Top left is 0,0
"text": "Create Account", 
"font": "Arial",
"fontsize": 35,
"hover_color": (80,80,80),
"main_color": (40,40,40),
"text_offset": 150,
"text_color": (255,255,255)
}
Log_in_btn = {
"width" : 500, # width of the button
"height" : 50, # height of the button
"StartPos": {"x" :  325,"y" : 430}, # Top left is 0,0
"text": "Log In", 
"font": "Arial",
"fontsize": 35,
"hover_color": (80,80,80),
"main_color": (40,40,40),
"text_offset": 200,
"text_color": (255,255,255)
}

def quit_btn(Lesson_btn):
    mouse = pygame.mouse.get_pos() # Stores mouse coordinates
    if Quit_btn['StartPos']['x'] <= mouse[0] <= Quit_btn['StartPos']['x'] + Quit_btn['width'] and Quit_btn['StartPos']['y'] <= mouse[1] <= Quit_btn['StartPos']['y']+Quit_btn['height']: 
        pygame.draw.rect(screen,Quit_btn['hover_color'],[Quit_btn['StartPos']['x'],Quit_btn['StartPos']['y'],Quit_btn['width'],Quit_btn['height']]) # If mouse is hovering
    else: 
        pygame.draw.rect(screen,Quit_btn['main_color'],[Quit_btn['StartPos']['x'],Quit_btn['StartPos']['y'],Lesson_btn['width'],Lesson_btn['height']]) # If mouse is not touching
    screen.blit(pygame.font.SysFont(Quit_btn['font'],Quit_btn['fontsize']).render(Quit_btn['text'] , True , Lesson_btn["text_color"]),(Lesson_btn['StartPos']['x']+Lesson_btn["text_offset"],Lesson_btn['StartPos']['y'])) # Putting text on the button

def account_create_btn(Account_create_btn):
    mouse = pygame.mouse.get_pos() # Stores mouse coordinates
    if Account_create_btn['StartPos']['x'] <= mouse[0] <= Account_create_btn['StartPos']['x'] + Account_create_btn['width'] and Account_create_btn['StartPos']['y'] <= mouse[1] <= Account_create_btn['StartPos']['y']+Account_create_btn['height']: 
        pygame.draw.rect(screen,Account_create_btn['hover_color'],[Account_create_btn['StartPos']['x'],Account_create_btn['StartPos']['y'],Account_create_btn['width'],Account_create_btn['height']]) # If mouse is hovering
    else: 
        pygame.draw.rect(screen,Account_create_btn['main_color'],[Account_create_btn['StartPos']['x'],Account_create_btn['StartPos']['y'],Account_create_btn['width'],Account_create_btn['height']]) # If mouse is not touching
    screen.blit(pygame.font.SysFont(Account_create_btn['font'],Account_create_btn['fontsize']).render(Account_create_btn['text'] , True , Account_create_btn["text_color"]),(Account_create_btn['StartPos']['x']+Account_create_btn["text_offset"],Account_create_btn['StartPos']['y'])) # Putting text on the button

def log_in_btn(Log_in_btn):
    mouse = pygame.mouse.get_pos() # Stores mouse coordinates
    if Log_in_btn['StartPos']['x'] <= mouse[0] <= Log_in_btn['StartPos']['x'] + Log_in_btn['width'] and Log_in_btn['StartPos']['y'] <= mouse[1] <= Account_create_btn['StartPos']['y']+Log_in_btn['height']: 
        pygame.draw.rect(screen,Log_in_btn['hover_color'],[Log_in_btn['StartPos']['x'],Log_in_btn['StartPos']['y'],Log_in_btn['width'],Log_in_btn['height']]) # If mouse is hovering
    else: 
        pygame.draw.rect(screen,Log_in_btn['main_color'],[Log_in_btn['StartPos']['x'],Log_in_btn['StartPos']['y'],Log_in_btn['width'],Log_in_btn['height']]) # If mouse is not touching
    screen.blit(pygame.font.SysFont(Log_in_btn['font'],Log_in_btn['fontsize']).render(Log_in_btn['text'] , True , Log_in_btn["text_color"]),(Log_in_btn['StartPos']['x']+Log_in_btn["text_offset"],Log_in_btn['StartPos']['y'])) # Putting text on the button


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
    screen.blit(title_text, title_rect)
    # Display the options
    quit_btn(Quit_btn)
    account_create_btn(Account_create_btn)
    log_in_btn(Log_in_btn)
    screen.blit(bird1, (30, 0)) # Draw the first bird image at (0, 0)
    screen.blit(bird2, (900,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if Quit_btn['StartPos']['x'] <= event.pos[0] <= Quit_btn['StartPos']['x'] + Quit_btn['width'] and Quit_btn['StartPos']['y'] <= event.pos[1] <= Quit_btn['StartPos']['y'] + Quit_btn['height']:
                # Go back to the main menu
                running = False

            elif Account_create_btn['StartPos']['x'] <= event.pos[0] <= Account_create_btn['StartPos']['x'] + Account_create_btn['width'] and Account_create_btn['StartPos']['y'] <= event.pos[1] <= Account_create_btn['StartPos']['y'] + Account_create_btn['height']:
                running = False

            elif Log_in_btn['StartPos']['x'] <= event.pos[0] <= Log_in_btn['StartPos']['x'] + Log_in_btn['width'] and Log_in_btn['StartPos']['y'] <= event.pos[1] <= Log_in_btn['StartPos']['y'] + Log_in_btn['height']:
                running = False
            

    

    pygame.display.flip()  # Update the display
    pygame.time.delay(100)  # Delay to control frame rate

# End of the game loop
final_message = "Thank you for playing!"
final_surface = font.render(final_message, True, (0, 0, 0))
screen.fill((255, 255, 255))  # Clear the screen for the final message
screen.blit(background_image, (0,0))
screen.blit(final_surface, (50, 50))
pygame.display.flip()  # Update the display
pygame.time.delay(2000)  # Wait for 2 seconds before quitting
# Quit Pygame
pygame.quit()
