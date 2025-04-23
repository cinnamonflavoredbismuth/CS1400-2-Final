import pygame
import csv

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
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
    screen.fill((255, 255, 255))  # Clear screen with white background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for i, rect in enumerate(button_rects):
                if rect.collidepoint(mouse_pos):
                    selected_option = i  # Set the selected option
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:  # Go to the next lesson
                current_lesson = min(current_lesson + 1, len(lessons) - 1)
                selected_option = -1  # Reset selection
            elif event.key == pygame.K_LEFT:  # Go to the previous lesson
                current_lesson = max(current_lesson - 1, 0)
                selected_option = -1  # Reset selection

    # Display the current lesson
    if lessons:
        lesson_title = font.render(f"Lesson {lessons[current_lesson][0]}: {lessons[current_lesson][1]}", True, (0, 0, 0))
        screen.blit(lesson_title, (50, 50))

        # Display the question
        question = font.render(lessons[current_lesson][2], True, (0, 0, 0))
        screen.blit(question, (50, 100))

        # Display the options as buttons
        for i, rect in enumerate(button_rects):
            option_text = lessons[current_lesson][3 + i]
            color = (0, 0, 255) if selected_option == i else (0, 0, 0)  # Highlight selected option
            pygame.draw.rect(screen, (200, 200, 200), rect)  # Draw button background
            pygame.draw.rect(screen, (0, 0, 0), rect, 2)  # Draw button border
            option = font.render(option_text, True, color)
            screen.blit(option, (rect.x + 10, rect.y + 5))

        # Check if the selected option is correct
        if selected_option != -1:
            correct_answer = lessons[current_lesson][7]  # Correct answer column
            feedback = "Correct!" if selected_option == int(correct_answer) else "Wrong!"
            feedback_text = font.render(feedback, True, (0, 128, 0) if feedback == "Correct!" else (255, 0, 0))
            screen.blit(feedback_text, (50, 400))

    pygame.display.flip()  # Update the display

# Quit Pygame
pygame.quit()