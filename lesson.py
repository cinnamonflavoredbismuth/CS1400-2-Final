import pygame
import csv
import random
import time
from basic_functions import btn,click,clear,pystart,if_clicked,button

# from sign_up_screen import * 

# Define the Spanish or Vanish game
# Initialize Pygame

# Set up the display
screen = pystart()


# Image background
bird1 = pygame.image.load("logo_uwu.png")     #Load Image
bird2 = pygame.image.load("logo_uwu.png")     #Load Image
bird2 = pygame.transform.flip(bird2, True, False)  # Flip the image horizontally
bird1 = pygame.transform.scale(bird1, (200, 200))  # Scale the image to fit the screen 
bird2 = pygame.transform.scale(bird2, (200, 200))  # Scale the image to fit the screen

def question_gather(unit, _lesson):
    questions = []
    with open('Lessons.csv', 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            if line[0] == unit:
                if line[1] == _lesson:
                    questions.append(line[2])
    return questions

def option_gather(unit, _lesson):
    options = []
    with open('Lessons.csv', 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            if line[0] == unit:
                if line[1] == _lesson:
                    options.append(line[3])
    return options

def answer_gather(question):
    answer = ""
    with open('Lessons.csv', 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            if question in line[2]:
                answer = line[3]
    return answer

def option_define(unit, _lesson):
    # Gather all options for the given unit and lesson
    options = option_gather(unit, _lesson)
    
    option1 = random.choice(options)
        
    option2 = random.choice(options)
        
    option3 = random.choice(options)
        
    option4 = random.choice(options)
        
    return option1, option2, option3, option4

def xoffset_gather(option):
    with open('Lessons.csv', 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            if option in line[3]:
                xoffset = line[4]
    return xoffset

def yoffset_gather(option):
    with open('Lessons.csv', 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            if option in line[3]:
                yoffset = line[5]
    return yoffset


#Create Button data

# Set up fonts
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 72)  # Larger font for the title



def lesson(unit, _lesson, correct, incorrect):
    questions = question_gather(unit, _lesson)
    question = random.choice(questions)
    answered_questions = correct + incorrect
    if len(answered_questions) == 5:
        question_text = title_font.render("All questions answered!", True, (0, 0, 0))
        question_rect = question_text.get_rect(center=(600, 100))  # Centered at the top of the screen
        clear()   #This Places the background
        screen.blit(question_text, question_rect)   #This will display the question
        pygame.display.flip()  # Update the display
        pygame.time.delay(2000)  # Wait for 2 seconds before quitting 
    option1, option2, option3, option4 = option_define(unit, _lesson)   
    
    question_text = title_font.render(question, True, (0, 0, 0)) # White color
    option3 = answer_gather(question)
    if question in correct or question:
        lesson(unit, _lesson, correct, incorrect)
    options = [option1, option2, option3, option4]
    random.shuffle(options)

    option1_btn = button(300,150,{"x" :  250,"y" : 330},options[0],"Arial",35,(200,200,200),(255,255,255), int(xoffset_gather(options[0])),int(yoffset_gather(options[0])),(50,50,50))
    
    option2_btn = button(300,150,{"x" :  650,"y" : 330},options[1],"Arial",35,(200,200,200),(255,255,255),int(xoffset_gather(options[1])),int(yoffset_gather(options[1])),(50,50,50))

    option3_btn = button(300, 150,{"x" :  250,"y" : 530},options[2],"Arial",35,(200,200,200),(255,255,255),int(xoffset_gather(options[2])), int(yoffset_gather(options[2])),(50,50,50))
            
    option4_btn = (300,150,{"x" :  650,"y" : 530}, options[3],"Arial",35,(200,200,200),(255,255,255),int(xoffset_gather(options[3])),int(yoffset_gather(options[3])),(50,50,50))
            
    quit_btn = (250,50,{"x" :  10,"y" : 730},"Quit", "Arial",35,(200,200,200),(255,255,255),90,0,(50,50,50))

     #Position the title at the top center of the screen
    question_rect = question_text.get_rect(center=(600, 100))  # Centered at the top of the screen

    while True:
        running = True
        while running:
            clear()
            screen.blit(question_text, question_rect)   #This will display the question

            #This is where we will call the buttons 
            btn(option1_btn)
            btn(option2_btn)
            btn(option3_btn)
            btn(option4_btn)
            btn(quit_btn)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if if_clicked(option1_btn,event) == True:
                        # Go back to the main menu
                        click()
                        if options[0] == option3:
                            question_text = title_font.render("Correct!", True, (0, 255, 0))
                            question_rect = question_text.get_rect(center=(600, 100))  # Centered at the top of the screen
                            clear()
                            screen.blit(question_text, question_rect)   #This will display the question
                            time.sleep(1)
                            correct.append(question)
                            lesson(unit, _lesson, correct, incorrect)
                        elif options[0] != option3:
                            question_text = title_font.render("Incorrect!", True, (0, 255, 0))
                            question_rect = question_text.get_rect(center=(600, 100))  # Centered at the top of the screen
                            clear()  #This Places the background
                            screen.blit(question_text, question_rect)   #This will display the question
                            time.sleep(1)
                            incorrect.append(question)
                            lesson(unit, _lesson, correct, incorrect)

                    elif if_clicked(option2_btn,event):
                        click()
                        if options[0] == option3:
                            question_text = title_font.render("Correct!", True, (0, 255, 0))
                            question_rect = question_text.get_rect(center=(600, 100))  # Centered at the top of the screen
                            clear()   #This Places the background
                            screen.blit(question_text, question_rect)   #This will display the question
                            time.sleep(1)
                            correct.append(question)
                            lesson(unit, _lesson, correct, incorrect)
                        elif options[0] != option3:
                            question_text = title_font.render("Incorrect!", True, (0, 255, 0))
                            question_rect = question_text.get_rect(center=(600, 100))  # Centered at the top of the screen
                            clear()  #This Places the background
                            screen.blit(question_text, question_rect)   #This will display the question
                            time.sleep(1)
                            incorrect.append(question)
                            lesson(unit, _lesson, correct, incorrect)
                        running = False

                    elif if_clicked(option3_btn,event) ==  True:
                        click()
                        if options[0] == option3:
                            question_text = title_font.render("Correct!", True, (0, 255, 0))
                            question_rect = question_text.get_rect(center=(600, 100))  # Centered at the top of the screen
                            clear()   #This Places the background
                            screen.blit(question_text, question_rect)   #This will display the question
                            time.sleep(1)
                            correct.append(question)
                            lesson(unit, _lesson, correct, incorrect)
                        elif options[0] != option3:
                            question_text = title_font.render("Incorrect!", True, (0, 255, 0))
                            question_rect = question_text.get_rect(center=(600, 100))  # Centered at the top of the screen
                            clear   #This Places the background
                            screen.blit(question_text, question_rect)   #This will display the question
                            time.sleep(1)
                            incorrect.append(question)
                            lesson(unit, _lesson, correct, incorrect)
                        running = False
                    
                    elif if_clicked(option4_btn,event) ==  True:
                        click()
                        if options[0] == option3:
                            question_text = title_font.render("Correct!", True, (0, 255, 0))
                            question_rect = question_text.get_rect(center=(600, 100))  # Centered at the top of the screen
                            clear()   #This Places the background
                            screen.blit(question_text, question_rect)   #This will display the question
                            time.sleep(1)
                            correct.append(question)
                            lesson(unit, _lesson, correct, incorrect)
                        elif options[0] != option3:
                            question_text = title_font.render("Incorrect!", True, (0, 255, 0))
                            question_rect = question_text.get_rect(center=(600, 100))  # Centered at the top of the screen
                            clear()   #This Places the background
                            screen.blit(question_text, question_rect)   #This will display the question
                            time.sleep(1)
                            incorrect.append(question)
                            lesson(unit, _lesson, correct, incorrect)
                        running = False

                    elif if_clicked(quit_btn,event) == True:
                        # Go back to the main menu
                        correct.clear()
                        incorrect.clear()
                        click()
                        running = False

                    
    
            pygame.display.flip()  # Update the display
            pygame.time.delay(100)  # Delay to control frame rat

        # End of the game loop
        final_message = "Thank you for playing!"
        final_surface = font.render(final_message, True, (0, 0, 0))
        clear()
        screen.blit(final_surface, (50, 50))
        pygame.display.flip()  # Update the display
        pygame.time.delay(2000)  # Wait for 2 seconds before quitting
        # Quit Pygame
        break
    
#lesson()
#print(question_gather())