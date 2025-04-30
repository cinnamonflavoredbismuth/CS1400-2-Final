# Miscellaneous

# Luke's dislocated Functions
import matplotlib.pyplot as plt

def accuracy_visual(correct, questions): # Displays a pie chart for the accuracy of an amount of questions with an amount of correctly answered ones
    
    correct_perc = round((int(correct) / int(questions)) * 100)
    data = [100-correct_perc, correct_perc] # Add up to 100
    labels = ['Incorrect', 'Correct']
    colors = ['tab:red', 'tab:green']
    explode = (0.1, 0)

    plt.pie(data, labels=labels, colors=colors, explode=explode, shadow=True, autopct='%1.0f%%')
    plt.title('Accuracy')
    plt.show()

def do_unit(): # 
    acc = load(name) #?
    # Get user's account info from csv file
    #if acc.unit == final quiz
    #     Set the quiz to have every question in its question bank
    # else:
    #     if user.unit ==  on and set the lesson and quiz for that unit
    #     # input(f"The lesson content:\n{}\nPress Enter to Continue\n")
    # lesson/quiz()

def social():
    accs = load_all()
    print("\nStreak Leaderboard\n")
    streaks = []
    for acc in accs:
        streaks.append([acc.streak, acc.name])
    ranked_streaks = sorted(streaks, key=lambda acc: int(acc[0]), reverse=True)
    for rank, streak in enumerate(ranked_streaks[:10]):
        print(f"{rank+1}. {streak[1]} - {streak[0]} days")