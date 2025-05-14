# Accuracy Graph -Luke Murdock
import matplotlib.pyplot as plt
from basic_functions import *

def accuracy_visual(correct, questions = 5): # Displays a pie chart for the accuracy of an amount of questions with an amount of correctly answered ones
    
    correct_perc = round((int(len(correct)) / questions) * 100)
    data = [100-correct_perc, correct_perc] # Add up to 100
    labels = ['Incorrect', 'Correct']
    colors = ['tab:red', 'tab:green']
    explode = (0.1, 0)

    plt.pie(data, labels=labels, colors=colors, explode=explode, shadow=True, autopct='%1.0f%%')
    plt.title('Accuracy')
    plt.show()
