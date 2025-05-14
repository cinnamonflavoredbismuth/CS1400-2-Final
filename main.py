import pygame
from stat_screen import lessons
from basic_functions import  display, start_up, bgm, if_clicked, clear, button, pystart, display_buttons, birds
from account_screens import new_account, get_log_in
from account_handler import load

# Define the Spanish or Vanish game
# This is a simple game where the user selects the correct answer from multiple options.
# The game will display a lesson and multiple options, and the user has to select the correct one.
# The game will be played using Pygame, a popular library for creating games in Python.

screen = pystart()

# Image background
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 72)  # Larger font for the title

buttons = {
'Quit_btn' :button(500, 50, {"x" :  325,"y" : 630},"Quit", "Arial", 35, (80,80,80), (40,40,40), 225, 0, (255,255,255),False),
'Account_create_btn' : button(500, 50, {"x" :  325,"y" : 530},"Create Account", "Arial", 35, (80,80,80), (40,40,40), 150, 0, (255,255,255),False),
'Log_in_btn' : button(500, 50, {"x" :  325,"y" : 430},"Log In", "Arial", 35, (80,80,80), (40,40,40), 200, 0, (255,255,255),False),
}
# Main loop
def main_menu(): # This creates the starting screen with the options of log_in, create_account, and quit.
    bgm()
    while True:
        running = True
        while running:
            clear()
            display_buttons(buttons)
            birds()
            title_text = title_font.render("Spanish or Vanish", True, (255, 255, 255))
            title_rect = title_text.get_rect(center=(575, 100))  # Centered at the top of the screen
            screen.blit(title_text, title_rect)   #This will display the question
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if if_clicked(buttons['Quit_btn'],event) == True: # If  quit button clicked
                        # Go back to the main menu
                        
                        running = False

                    elif if_clicked(buttons['Account_create_btn'],event) == True: # If Account Create button clicked
                        
                        name=new_account()
                        if name == None:
                            main_menu()
                        else:
                            acc=load(name)
                            print(acc)
                            lessons(acc)

                    elif if_clicked(buttons['Log_in_btn'],event) == True: # If Log In button clicked
                        #name = get_log_in()
                        name = 'cecily'
                        acc = load(name)
                        lessons(acc)

            pygame.display.flip()  # Update the display
            pygame.time.delay(100)  # Delay to control frame rate


        #display("Thank you for playing!",2) ----------------------------------------------------------------------------------------
        pygame.quit()
        break

def main(): # Plays start up sound and then starts the program's main menu
    start_up()
    main_menu()

main()
