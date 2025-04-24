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

# Set up fonts
font = pygame.font.Font(None, 36)

# Load lessons and questions from CSV
lessons = []
with open('lessons.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        lessons.append(row)

# Start with the first lesson
current_lesson = 0
selected_option = -1  # No option selected initially

# Define button positions
button_rects = [
    pygame.Rect(50, 150, 700, 40),  # Option 1
    pygame.Rect(50, 200, 700, 40),  # Option 2
    pygame.Rect(50, 250, 700, 40),  # Option 3
    pygame.Rect(50, 300, 700, 40),  # Option 4
]


# Main loop
running = True
while running:
    screen.fill((255, 255, 255))  # Clear the screen with a white background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()  # Get mouse position
            for i, rect in enumerate(button_rects):
                if rect.collidepoint(mouse_pos):  # Check if mouse click is inside a button
                    selected_option = i  # Update selected option

    # Display the options
    for i, option in enumerate(lessons[current_lesson][1:]):
        option_surface = font.render(option, True, (0, 0, 0))
        screen.blit(option_surface, (50, 150 + i * 50))
        if selected_option == i:
            pygame.draw.rect(screen, (255, 0, 0), button_rects[i], 2)  # Highlight selected option
        else:
            pygame.draw.rect(screen, (0, 0, 0), button_rects[i], 2)

    # Draw the buttons
    for rect in button_rects:
        pygame.draw.rect(screen, (0, 0, 0), rect, 2)  # Draw the button outline

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
