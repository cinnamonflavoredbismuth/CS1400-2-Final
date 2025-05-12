import pygame
import csv
import random
from spanish import lessons
from basic_functions import  display, start_up, bgm, if_clicked, clear, button, pystart, display_buttons
from basic_functions import *
from account_screens import new_account, get_log_in
from account_handler import load

# Define the Spanish or Vanish game
# This is a simple game where the user selects the correct answer from multiple options.
# The game will display a lesson and multiple options, and the user has to select the correct one.
# The game will be played using Pygame, a popular library for creating games in Python.

screen = pystart()

# Image background

buttons={
'Quit_btn' :button(500, 50, {"x" :  325,"y" : 630},"Quit", "Arial", 35, (80,80,80), (40,40,40), 225, 0, (255,255,255)),
'Account_create_btn' : button(500, 50, {"x" :  325,"y" : 530},"Create Account", "Arial", 35, (80,80,80), (40,40,40), 150, 0, (255,255,255)),
'Log_in_btn' : button(500, 50, {"x" :  325,"y" : 430},"Log In", "Arial", 35, (80,80,80), (40,40,40), 200, 0, (255,255,255)),
}
# Main loop
def main_menu():
    bgm()
    while True:
        running = True
        while running:
            clear()
            display_buttons(buttons)
            birds()
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


        #display("Thank you for playing!",3)
        pygame.quit()
        break

def main():
    start_up()
    main_menu()

main()
