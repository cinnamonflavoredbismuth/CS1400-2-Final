# Miscellaneus
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



def display_streaks(acc):
    screen=pystart()
    font = pygame.font.Font(None, 36)

    surface = font.render(f"Your streak is: {acc.streak}", True, (0, 0, 0))
    screen.blit(surface, (50, 50))


def leaderboard():
    accs=[]
    with open("users.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            accs.append(User(line[0], line[1], line[2], line[3], line[4], line[5], line[6]))

    print("\nStreak Leaderboard\n")
    streaks = []
    for acc in accs:
        streaks.append([acc.streak, acc.name])
    ranked_streaks = sorted(streaks, key=lambda acc: int(acc[0]), reverse=True)
    for rank, streak in enumerate(ranked_streaks[:10]):
        print(f"{rank+1}. {streak[1]} - {streak[0]} days")