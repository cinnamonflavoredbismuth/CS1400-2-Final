import pygame
import csv
import random
import time
import matplotlib.pyplot
from basic_functions import pystart, clear, button, display_buttons, if_clicked,display
from graphs import accuracy_visual  # Assuming you have a graphs.py file with the necessary functions
from account_handler import load
# from sign_up_screen import * 

# Define the Spanish or Vanish game
# Initialize Pygame

# Set up the display
screen = pystart()



def question_gather(unit, _lesson): # 
    questions = []
    if _lesson != 'quiz':
        with open('csv_files/Lessons.csv', 'r') as file:
            reader = csv.reader(file)
            for line in reader:
                if line[0] == unit:
                    if line[1] == _lesson:
                        questions.append(line[2])
                    else:
                        continue
                else:
                    continue
            if len(questions) == 5:
                    return questions
    else:
        with open('csv_files/Lessons.csv', 'r') as file:
            reader = csv.reader(file)
            for line in reader:
                if line[0] == unit:
                        questions.append(line[2])
                else:
                    continue
            if len(questions) == 35:
                    return questions
                    
def option_gather(unit, _lesson): # 
    options = []
    if _lesson != 'quiz':
        with open('csv_files/Lessons.csv', 'r') as file:
            reader = csv.reader(file)
            for line in reader:
                if line[0] == unit:
                    if line[1] == _lesson:
                        options.append(line[3])
                        if len(options) == 5:
                            return options
    else:
        with open('csv_files/Lessons.csv', 'r') as file:
            reader = csv.reader(file)
            for line in reader:
                if line[0] == unit:
                    options.append(line[3])
                    if len(options) == 5:
                        return options
    return options

def answer_gather(question): # 
    answer = ""
    with open('csv_files/Lessons.csv', 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            if question in line[2]:
                answer = line[3]
    return answer

def option_define(unit, _lesson,question): # 
    # Gather all options for the given unit and lesson
    options = option_gather(unit, _lesson)
    
    option1 = random.choice(options)
        
    option2 = random.choice(options)
        
    option3 = answer_gather(question)
        
    option4 = random.choice(options)

    while option1 == option2 or option1 == option3 or option1 == option4 or option2 == option3 or option2 == option4 or option3 == option4:
        option1 = random.choice(options)
        option2 = random.choice(options)
        option3 = answer_gather(question)
        option4 = random.choice(options)
    return option1, option2, option3, option4

def xoffset_gather(option): # 
    with open('csv_files/Lessons.csv', 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            if option in line[3]:
                xoffset = line[4]
    return xoffset

def yoffset_gather(option): # 
    with open('csv_files/Lessons.csv', 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            if option in line[3]:
                yoffset = line[5]
    return yoffset

def option_chosen(msg): # 
    clear()
    display(msg, 0, 450, 100)
    time.sleep(1)

def get_questions(unit, _lesson,correct, incorrect): #
    questions = question_gather(unit, _lesson)
    question = random.choice(questions)
    option1, option2, option3, option4 = option_define(unit, _lesson, question)
    while question in correct or question in incorrect:
        questions = question_gather(unit, _lesson)
        question = random.choice(questions)
        option1, option2, option3, option4 = option_define(unit, _lesson, question)

    return option1, option2, option3, option4, question

#Create Button data

# Set up fonts
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 72)  # Larger font for the title



def lesson(unit, _lesson, correct, incorrect,acc): # Lets the user do a lesson
    lesson_complete = False
    answered_questions = correct + incorrect
    #print(answered_questions)
    if _lesson != 'quiz':
        if len(answered_questions) >= 5:
            # Set state
            results_screen = True

            # Create buttons once
            graph_button = {
                'graph_btn': button(300, 150, {"x": 450, "y": 430}, "Display Accuracy", "Arial", 35, (200, 200, 200), (255, 255, 255), 15, 60, (50, 50, 50), False),
                'quit_btn': button(300, 50, {"x": 10, "y": 730}, "Quit", "Arial", 35, (200, 200, 200), (255, 255, 255), 90, 0, (50, 50, 50), False)
            }

            while results_screen:
                clear()
                # Draw the message
                question_text = title_font.render("You completed your lesson!", True, (0, 0, 0))
                screen.blit(question_text, question_text.get_rect(center=(600, 100)))

                display_buttons(graph_button)
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        acc.streak_update()
                        pygame.quit()
                        exit()

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if if_clicked(graph_button['graph_btn'], event):
                            clear()
                            accuracy_visual(correct) 
                            pygame.display.flip()
                            pygame.time.delay(1000)
                            lesson_complete = True

                        elif if_clicked(graph_button['quit_btn'], event):
                            acc.streak_update()
                            results_screen = False  # Exit this screen
                            correct.clear()
                            incorrect.clear()
                            lesson_complete = True  # Exit the lesson
    else:
        if len(answered_questions) >= 35:
            # Set state
            results_screen = True

            # Create buttons once
            graph_button = {
                'graph_btn': button(300, 150, {"x": 450, "y": 430}, "Display Accuracy", "Arial", 35, (200, 200, 200), (255, 255, 255), 15, 60, (50, 50, 50), False),
                'quit_btn': button(300, 50, {"x": 10, "y": 730}, "Quit", "Arial", 35, (200, 200, 200), (255, 255, 255), 90, 0, (50, 50, 50), False)
            }

            while results_screen:
                clear()
                # Draw the message
                question_text = title_font.render("You completed your Quiz!", True, (0, 0, 0))
                screen.blit(question_text, question_text.get_rect(center=(600, 100)))

                display_buttons(graph_button)
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        acc.streak_update()
                        pygame.quit()
                        exit()

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if if_clicked(graph_button['graph_btn'], event):
                            clear()
                            accuracy_visual(correct) 
                            pygame.display.flip()
                            pygame.time.delay(1000)

                        elif if_clicked(graph_button['quit_btn'], event):
                            acc.streak_update()
                            results_screen = False  # Exit this screen
                            correct.clear()
                            incorrect.clear()

        if lesson_complete == False:
            option1, option2, option3, option4, question = get_questions(unit, _lesson,correct, incorrect)
            options = [option1, option2, option3, option4]
            random.shuffle(options)
            buttons={
            'option1_btn' : button(300,150,{"x" :  250,"y" : 330},options[0],"Arial",35,(200,200,200),(255,255,255), int(xoffset_gather(options[0])),int(yoffset_gather(options[0])),(50,50,50),False),
            'option2_btn' : button(300,150,{"x" :  650,"y" : 330},options[1],"Arial",35,(200,200,200),(255,255,255),int(xoffset_gather(options[1])),int(yoffset_gather(options[1])),(50,50,50),False),
            'option3_btn' :button(300, 150,{"x" :  250,"y" : 530},options[2],"Arial",35,(200,200,200),(255,255,255),int(xoffset_gather(options[2])), int(yoffset_gather(options[2])),(50,50,50),False),
            'option4_btn' : button(300,150,{"x" :  650,"y" : 530}, options[3],"Arial",35,(200,200,200),(255,255,255),int(xoffset_gather(options[3])),int(yoffset_gather(options[3])),(50,50,50),False),
            
            'quit_btn': button(250,50,{"x" :  10,"y" : 730},"Quit", "Arial",35,(200,200,200),(255,255,255),90,0,(50,50,50),False)
            }
            while True:
                running = True
                clear()
                while running:
                    display(question, 0, 450, 100)
                    #This is where we will call the buttons 
                    display_buttons(buttons)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if if_clicked(buttons['option1_btn'],event) == True:
                                # Go back to the main menu
                                
                                if options[0] == option3:
                                    clear()
                                    option_chosen('Correct!')
                                    correct.append(question)
                                    lesson(unit, _lesson, correct, incorrect,acc)
                                elif options[0] != option3:
                                    clear()
                                    option_chosen('Incorrect!')
                                    incorrect.append(question)
                                    lesson(unit, _lesson, correct, incorrect,acc)

                            elif if_clicked(buttons['option2_btn'],event) == True:
                                if options[1] == option3:
                                    clear()
                                    option_chosen('Correct!')
                                    correct.append(question)
                                    lesson(unit, _lesson, correct, incorrect,acc)
                                elif options[1] != option3:
                                    clear()
                                    option_chosen('Incorrect!')
                                    incorrect.append(question)
                                    lesson(unit, _lesson, correct, incorrect,acc)

                            elif if_clicked(buttons['option3_btn'],event) == True:
                                if options[2] == option3:
                                    clear()
                                    option_chosen('Correct!')
                                    correct.append(question)
                                    lesson(unit, _lesson, correct, incorrect,acc)
                                elif options[2] != option3:
                                    clear()
                                    option_chosen('Incorrect!')
                                    incorrect.append(question)
                                    lesson(unit, _lesson, correct, incorrect,acc)

                            elif if_clicked(buttons['option4_btn'],event) == True:
                                if options[3] == option3:
                                    clear()
                                    option_chosen('Correct!')
                                    correct.append(question)
                                    lesson(unit, _lesson, correct, incorrect,acc)
                                elif options[3] != option3:
                                    clear()
                                    option_chosen('Incorrect!')
                                    incorrect.append(question)
                                    lesson(unit, _lesson, correct, incorrect,acc)
                            elif if_clicked(buttons['quit_btn'],event) == True:
                                # Go back to the main menu
                                correct.clear()
                                incorrect.clear()
                                
                                running = False


                    pygame.display.flip()  # Update the display
                    pygame.time.delay(100)  # Delay to control frame 
                break

    # End of the game loop
    display("Thank you for playing!", 0, 450, 100)

# FOR TESTING
acc=load('cecily')
print(lesson('Basics',' 1',[],[],acc))