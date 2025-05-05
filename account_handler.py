
# Account Handler -Cecily Strong,  Luke
from datetime import datetime, timedelta
import csv

class User: # 
    def __init__(self, name,password,unit,lesson,streak,date,lives): # 
        self.name = name
        self.password = password
        self.unit = unit
        self.lesson = lesson
        self.streak = streak
        self.date = date
        self.lives = lives

    def basic(self): # Basic account for new users
        self.unit=0
        self.lesson=1
        self.streak=0
        self.date = datetime.today()
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
    Lives left: {self.lives}
    Lesson: {self.lesson}"""

    def export(self): # used to save account info to csv
        return (self.name,self.password,self.unit,self.lesson,self.streak,datetime.today(),self.lives)

    def display_streak(self): # displays streak
        # Get user's account info from csv file
        input(f"Your streak is: {self.streak}\nPress Enter to Continue\n")

    def edit(self,delete=False): # FIX THIS LATER
        toWrite = []
        with open("users.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == self.name:
                    if delete==False:
                        exported=self.export()
                        toWrite.append({'name':exported[0], 'password':exported[1], 'unit':exported[2], 'lesson':exported[3], 'streak':exported[3], 'date':exported[4], 'lives':exported[5]})
                    else: pass
                else:
                    toWrite.append({'name':row[0], 'password':row[1], 'unit':row[2], 'lesson':row[3], 'streak':row[4], 'date':row[5], 'lives':row[6]})
        print(toWrite)
        with open("users.csv", "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "password", "unit", "lesson", "streak", "date", "lives"])
            writer.writerows(toWrite)



def load(name): # loads account from csv
    with open("users.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            if line[0] == name:
               user = User(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
               return user
        else: # stupid proofing
            #print("Account not found.")
            return False
        
def load_all(): # loads all accounts from csv
    accs=[]
    with open("users.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            accs.append(User(line[0], line[1], line[2], line[3], line[4], line[5], line[6]))
            return accs

def new_account(name,password): # 
    name=name.strip()
    password=password.strip()
    acc=User(name,password,1,1,0,datetime.today(),3)
    acc.basic()
    exists=load(name)
    if exists==False:
        with open("users.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(acc.export())
        print('account successfully created')
    else:
        print('account already exists')
        return False
   
def log_in(name, password): # Checks to see if the user's inputted account exists
    accs = load_all()
    for acc in accs:
        if acc.name == name and acc.pasword == password:
            return True
    return False