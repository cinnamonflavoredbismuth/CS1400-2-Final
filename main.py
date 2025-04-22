# Program  -Cecily Strong, Luke Murdock, Tate Morgan, Hasan De La Cruz
# Main File -Luke Murdock
from class import Account

def menu(): # Introduces the program and then lets the user choose one of the options
     
    while True:
        choice = input("\nWhat would you like to do?:\n1. \n2. \n3. \n4. \n5. \n6. \n7. Log out\n\nChoice: ").strip()
        if choice == '1':
            ()
            pass
        elif choice == '2':
            ()
        elif choice == '3':
            ()
        elif choice == '4':
            ()
        elif choice == '5':
            ()
        elif choice == '6':
            ()
        elif choice == '7':
            print("You have logged out")
            break
        else:
            print("\nInvalid Input (Insert a Corresponding Number)")

def sign_in(): # 
    accounts = read_file()
    for account in accounts:
        account["Active"] = False
    while True:
        choice = input("\nWhat would you like to do?:\n1. Log in\n2. Sign up\n3. Quit\n\nChoice: ").strip()
        if choice == '1':
            found = False
            user_name = input('\nUsername: ').strip()
            password = input('Password: ').strip()
            for ind, user in enumerate(user_profiles):
                if user_name == user['Name'] and password == user['Password']:
                    user_profiles[ind]["Active"] = True
                    write_file(user_profiles)
                    print('\nYou have logged in!')
                    found = True
                    menu()
                    user_profiles = read_file()
            if found == False:
                print('\nUsername or password couldn\'t be found')
                continue
        elif choice == '2':
            sign_up_user_name = input('\nusername: ').strip()
            check = False
            for user in user_profiles:
                if sign_up_user_name == user['Name']:
                    print('\nThat username has already been taken.\n')
                    check = True
            if check == True:
                continue       
            sign_up_password = input('\npassword: ').strip()
            
            account = Account()
            user_profiles.append(profile)
            write_file(user_profiles)
            print("\nCreated new profile") #Now they go back and can go log in to that account

        elif choice == '3':
            print('\n\nThank you for using this program!\n\n\n')
            exit()
        else:
            print('\nInvalid Input (Insert a Corresponding Number)')
            
            
print("\n\n\nWelcome to this Program, where you can .")
sign_in()



from pet_class import random
from file_handler import read_file, write_file, active_pet
from pet_handler import ask_new_pet, display_pets, breed

def menu(): # Lets the user choose one of the options and then might randomly pick a random event to enact
    pets = read_file()
    pet = active_pet(pets)

    while True:
        choice = input(f"\nWhat do you want to do with your pet named {pets[pet].name}?\nView status(1) Pet(2) Feed(3) Play(4) Compete(5) Shop(6) Sleep(7) Breed(8)  Exit(0)\nChoice: ").strip()
        if choice == '0':
            pets[pet].active = False
            write_file(pets)
            break
        elif choice == '1':
            pets[pet].status()
        elif choice == '2':
            print(pets[pet].pet())
        elif choice == '3':
            print(pets[pet].feed())
        elif choice == '4':
            print(pets[pet].play())
        elif choice == '5':
            print(pets[pet].competition())
        elif choice == '6':
            print(pets[pet].shop())
        elif choice == '7':
            print(pets[pet].sleep())
        elif choice == '8':
            print(breed())
            pets = read_file()
        else:
            print("\nInvalid Input (Insert a Corresponding Number)")
        write_file(pets)



def pick_pet(): # Lets a user get new pets and pick which one they want to interact with
    pets = read_file()
    for ind, pet in enumerate(pets):
        pets[ind].active = False
    write_file(pets)
    while True:
        choice = input("\nGet a pet(1) Interact with a pet(2)  Quit(3)\nChoice: ").strip()
        if choice == '1':
            print(ask_new_pet())
        elif choice == '2':

            def pick_interact_pet(): # Picks the pet the user wanted if it exists and then goes to the menu
                nonlocal pets
                name = display_pets(pets)
                for ind, pet in enumerate(pets):
                    if name.lower() == pet.name.lower():
                        pets[ind].active = True
                        write_file(pets)
                        print(f'\nYou have successfully picked your pet, {pets[ind].name}!')
                        return True
                print(f'\nThe pet "{name}" could not be found')
                return False
                    
            if pick_interact_pet() == True:
                menu()

        elif choice == '3':
            print("\n\n\nThank you for using this Pet Simulator!\nCome Back Soon!\n\n\n")
            exit()
        else:
            print('\nInvalid Input (Insert a Corresponding Number)')
        pets = read_file()