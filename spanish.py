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
pygame.display.set_icon()
pygame.display.set_icon(pygame.image.load('logo.jpg'))


# Set up fonts
font = pygame.font.Font(None, 36)


#Set up buttons
Lesson_btn = {
"width" : 140, # width of the button
"height" : 40, # height of the button
"StartPos": {"x" :  270,"y" : 630}, # Top left is 0,0
"text": "Menu", 
"font": "Arial",
"fontsize": 35,
"hover_color": (80,80,80),
"main_color": (40,40,40),
"text_offset": 0,
"text_color": (255,255,255)
}
def lesson_btn(Lesson_btn):
    mouse = pygame.mouse.get_pos() # Stores mouse coordinates
    if Lesson_btn['StartPos']['x'] <= mouse[0] <= Lesson_btn['StartPos']['x'] + Lesson_btn['width'] and Lesson_btn['StartPos']['y'] <= mouse[1] <= Lesson_btn['StartPos']['y']+Lesson_btn['height']: 
        pygame.draw.rect(screen,Lesson_btn['hover_color'],[Lesson_btn['StartPos']['x'],Lesson_btn['StartPos']['y'],Lesson_btn['width'],Lesson_btn['height']]) # If mouse is hovering
    else: 
        pygame.draw.rect(screen,Lesson_btn['main_color'],[Lesson_btn['StartPos']['x'],Lesson_btn['StartPos']['y'],Lesson_btn['width'],Lesson_btn['height']]) # If mouse is not touching
    screen.blit(pygame.font.SysFont(Lesson_btn['font'],Lesson_btn['fontsize']).render(Lesson_btn['text'] , True , Lesson_btn["text_color"]),(Lesson_btn['StartPos']['x']+Lesson_btn["text_offset"],Lesson_btn['StartPos']['y'])) # Putting text on the button


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
    # Display the options
    lesson_btn(Lesson_btn)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if Lesson_btn['StartPos']['x'] <= event.pos[0] <= Lesson_btn['StartPos']['x'] + Lesson_btn['width'] and Lesson_btn['StartPos']['y'] <= event.pos[1] <= Lesson_btn['StartPos']['y'] + Lesson_btn['height']:
                # Go back to the main menu
                running = False
            

    

    pygame.display.flip()  # Update the display
    pygame.time.delay(100)  # Delay to control frame rate

# End of the game loop
final_message = "Thank you for playing!"
final_surface = font.render(final_message, True, (0, 0, 0))
screen.fill((255, 255, 255))  # Clear the screen for the final message
screen.blit(final_surface, (50, 50))
pygame.display.flip()  # Update the display
pygame.time.delay(2000)  # Wait for 2 seconds before quitting
# Quit Pygame
pygame.quit()
