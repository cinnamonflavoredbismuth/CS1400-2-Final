# Program  -Cecily Strong, Luke Murdock, Tate Morgan, Hasan De La Cruz
# Main File -Luke Murdock
from user_class import User

def menu(): # Introduces the program and then lets the user choose one of the options
    # accs = read_file()
    # acc = active_pet(accs)

    while True:
        choice = input("\nWhat would you like to do?:\n1. \n2. \n3. \n4. \n5. \n6. \n7. Log out\n\nChoice: ").strip()
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

def sign_in(): # 
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
            new_name = input('\nusername: ').strip()
            check = False
            for acc in accs:
                if new_name == acc.accs:
                    print('\nThat username has already been taken.\n')
                    check = True
            if check == True:
                continue       
            new_password = input('\npassword: ').strip()

            new_acc = User(new_name, new_password, )
            # user_profiles.append(new_acc)
            # write_file(user_accs)
            print("\nCreated new account") # Now they can log into that account
            
        elif choice == '3':
            print('\n\nThank you for using this program!\n\n\n')
            exit()
        else:
            print('\nInvalid Input (Insert a Corresponding Number)')
            
            
print("\n\n\nWelcome to this Program, where you can .")
sign_in()