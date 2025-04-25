# Account Handler -Cecily Strong,  Luke
from datetime import datetime, timedelta
import csv
import matplotlib.pyplot as plt

class User: # 
    def __init__(self, name,password,unit,lesson,streak,date,lives): # 
        self.name = name
        self.password = password
        self.unit = unit
        self.lesson = lesson
        self.streak = streak
        self.date = date
        self.lives = lives

    def basic(self,name,password): # Basic account for new users
        self.name=name
        self.password=password
        self.unit=0
        self.lesson=1
        self.streak=0
        self.date = datetime.now()
        self.lives=3 # default lives for new users

    def subtract_life(self): #subtract life 
        if self.lives > 0:
            self.lives -= 1
        else:
            print("No lives left")
            # return to main menu or exit

    def streak_update(self): #update streak
        yesterday = datetime.now() - timedelta(1)
        if self.date == yesterday:
            self.streak=int(self.streak)+1
        else:
            self.streak=0
            self.subtract_life()

    def unit_update(self, unit): #update unit
        self.unit = unit

    def lesson_update(self, lesson): #update lesson
        self.lesson = lesson

    def __str__(self): #Show account info
        return f"""
Name: {self.name}
    Password: {self.password}
    Unit: {self.unit}
    Streak: {self.streak} days
    Streak last updated: {self.date}
    Lives left{self.lives}
    Lesson: {self.lesson}"""

    def export_dic(self): # used to save account info to csv
        return f"{self.name},{self.password},{self.unit},{self.lesson},{self.streak},{self.date},{self.lives}"

    def display_streak(self): # displays streak
    def update_streak(self): # 
        pass
        # if self.date == yesterday's date
            # self.streak + 1
        # else:
        #     user.streak = 0
        #     user.date = current date

        # ----------Luke's Rough Code -----------
        # Get user's account info from csv file
        # IF today's date isn't already saved to their account
        #     Add 1 to the active user's streak
        #     Save today's date to their account

    def display_streak(): # 
        pass
        # Get user's account info from csv file
        input(f"Your streak is: {self.streak}\nPress Enter to Continue\n")
        # input(f"Your streak is: {self.streak}\nPress Enter to Continue\n")


def load_account(name): # loads account from csv
    with open("users.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            if line[0] == name:
               user = User(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
               return user
        else: # stupid proofing
            print("Account not found.")
            return False

def edit_account(): # 
    pass
    # get name from user
    # open account csv as read
    # for line in csv
    #     if the name on line is name:
    #         save line to user class
    #         user.update_streak
    #         save user.export_dic to dic
    #     else: 
    #         save line to dic
    # open acc as write
    #     dict write the updated information

def new_account(): # 
    pass
    # get name and other info (password) from user
    # user is user(name,0,0,date)
    # open account csv as append
    #     write line from user

    # ----------Luke's Rough Code -----------
    # new_name = input('\nusername: ').strip()
    # check = True
    # for acc in accs:
    #     if new_name == acc.accs:
    #         print('\nThat username has already been taken.\n')
    #         check = False
    # if check == True:
    #     continue       
    # new_password = input('\nPassword: ').strip()

    # new_acc = User(new_name, new_password, )

    # # Adding to file
    # # user_profiles.append(new_acc)
    # # write_file(user_accs)


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

def do_unit(): # 
    pass
    # Get user's account info from csv file
    #if acc.unit == final quiz
    #     Set the quiz to have every question in its question bank
    # else:
    #     if user.unit ==  on and set the lesson and quiz for that unit
    #     # input(f"The lesson content:\n{}\nPress Enter to Continue\n")
    # lesson/quiz()