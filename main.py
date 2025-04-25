# Program  -Cecily Strong, Luke Murdock, Tate Morgan, Hasan De La Cruz
# Main File -Luke Murdock
from user_class import User
from spanish import game
from account_handler import User, load_account, edit_account, new_account


# Finish
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
        # write_file(pets)

# Finish
def sign_in(): # Lets the user sign up if they don't have an account and log in if they do, and once logged in will bring them to the menu
    # accs = read_file()
    # for acc in acc:
    #     acc.active = False
    while True:
        choice = input("\nWhat would you like to do?:\n1. Log in\n2. Sign up\n3. Quit\n\nChoice: ").strip()
        if choice == '1':

            def log_in(): # Logs the user in with their inputted info and then goes to the menu
                # nonlocal 
                name = input('\nUsername: ').strip()
                password = input('Password: ').strip()
                for ind, acc in enumerate(accs):
                    if name.lower() == acc.name.lower() and password == acc.password:
                        # accs[ind].active = True
                        # write_file(accs)
                        print('\nYou have logged in as {name}!')
                        return True
                print(f'\nUsername or password could not be found')
                return False
                    
            if log_in() == True:
                menu()

        elif choice == '2':
            # Finish
            new_account()
            print("\nCreated new account") # Now they can log into that account
            
        elif choice == '3':
            print('\n\nThank you for using Spanish or Vanish!\n\n\n')
            exit()
        else:
            print('\nInvalid Input (Insert a Corresponding Number)')
            
            
print("\n\n\nWelcome to Spanish or Vanish, where you can do lessons everyday to keep up your streak and .")
sign_in()