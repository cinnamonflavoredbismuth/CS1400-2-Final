# Miscellaneus
import csv
import pygame
import matplotlib.pyplot as plt
from basic_functions import pystart

# Luke's dislocated Functions
def accuracy_visual(correct, questions): # Displays a pie chart for the accuracy of an amount of questions with an amount of correctly answered ones
    
    correct_perc = round((int(correct) / int(questions)) * 100)
    data = [100-correct_perc, correct_perc] # Add up to 100
    labels = ['Incorrect', 'Correct']
    colors = ['tab:red', 'tab:green']
    explode = (0.1, 0)

    plt.pie(data, labels=labels, colors=colors, explode=explode, shadow=True, autopct='%1.0f%%')
    plt.title('Accuracy')
    plt.show()


# from basic_functions import button

# Board = button(500, 50, {"x" :  325,"y" : 430},"Log In", "Arial", 35, (80,80,80), (40,40,40), 200, 0, (255,255,255))
# print(Board)