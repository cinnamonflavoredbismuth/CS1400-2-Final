# Program  -Cecily Strong, Luke Murdock, Tate Morgan, Hasan De La Cruz
# Main File -Luke Murdock
from stat import *
from account_handler import *


'''# Finish
def menu(): # Introduces the program and then lets the user choose one of the options
    # accs = read_file()
    # acc = active_pet(accs)

    while True:
        choice = input("\nWhat would you like to do?:\n1. Display Streak\n2. Play(?)\n3. \n4. \n5. \n6. \n7. Log out\n\nChoice: ").strip()
        if choice == '1':
            acc.()
        elif choice == '2':
            acc.()
        elif choice == '3':
            acc.()
        elif choice == '4':
            acc.()
        elif choice == '5':
            acc.()
        elif choice == '6':
            acc.()
        elif choice == '7':
            print("You have logged out")
            break
        else:
            print("\nInvalid Input (Insert a Corresponding Number)")
        # write_file(pets)'''

# Finish
def sign_in(): # Lets the user sign up if they don't have an account and log in if they do, and once logged in will bring them to the menu
    
    while True:
        choice = input("\nWhat would you like to do?:\n1. Log in\n2. Sign up\n3. Quit\n\nChoice: ").strip()
        if choice == '1':
            name = input('\nUsername: ').strip()
            password = input('Password: ').strip()

            if log_in(name, password) == True:
                print(f'\nYou have logged in as {name}!')
                acc = load(name)
                menu(acc)
            else:
                print(f'\nUsername or password could not be found')
                
        elif choice == '2':
            name = input('\nUsername: ').strip()
            password = input('Password: ').strip()
            new_account(name,password)
            
        elif choice == '3':
            print('\n\nThank you for using Spanish or Vanish!\n\n\n')
            exit()
        else:
            print('\nInvalid Input (Insert a Corresponding Number)')
            
            
print("\n\n\nWelcome to Spanish or Vanish, where you can do lessons everyday to keep up your streak and .")
sign_in()