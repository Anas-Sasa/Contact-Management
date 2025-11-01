# Contact Managment [ 28 Mei 2024 ]

# Exercise on Ditctionaries
# Exercise on nested If statement
# Exercise on functions


contacts = {}

def edit_data():

    if contacts == {}:
        print('\nContacts is empty there is nothing to edit:\nPlease add a contact:\n')

    else:
        print('\nEdit a contact:\n_____\n')

        contact_id = input('\nEnter the contact [id]:  ')

        if contact_id.isdigit():

            if  contact_id != contacts['user_id']:
                print(f'\nID number ({contact_id}) is not exist:\n')

            else:  
                edit_name = input("\nEnter the contact new name:  ").title()

                if len(edit_name) >=1:

                    edit_phone_num = input('\nEnter a new phone number:  ')

                    if edit_phone_num.isdigit(): 

                        contacts['phone'] = edit_phone_num
                        contacts['name'] = edit_name
                    else:
                        print(f'\nYour input phone ({edit_phone_num}) not a digit:\n')
                   
                    if edit_name == contacts['name'] and edit_phone_num == contacts['phone']:
                        
                        print('\nEdits was successfully!\nYou can check your new contact!\n\n')
        
                    else:
                        print(f"Please enter the required data:\nTry after 2 minutes")

                else:
                    print('\nYou did not enter a name!\n\n')

        else:
            print(f'Your input ({contact_id}) is not a digit:\nWe accepte only digits. Try again!')
  
def add_data():

    print('\n\nAdd a contact;\n_____\n')

    name = input("\nEnter name:  ").title()

    if name.isalpha():

        phone_num = (input("\nEnter a phone number:  "))

        if phone_num.isdigit():

            id = (input('\nEnter an ID of contact:  '))
            
            if id.isdigit():

                contacts['name'] = name
                contacts['phone'] = phone_num
                contacts['user_id'] = id 
            else:
                    print(f"Id [{id}] is not acceptable!\n\n")

        else:
            print(f'Phone number ({phone_num}) is not acceptable!\nTry again:\n ')


        if len(contacts) == 3:
                print('\nAdd was successfully\n')
        else:
            print('\nAdd was not seccfully:\nTry again:\n') 

    else:
            print(f'Entry [ {name} ] is not acceptable!\nYou only can enter characters!\n')


game_on = True

while game_on:

    print("\n\nContact Management;\n_____\n")
    print('1- Add a contact\n')
    print('2- View contacts\n')
    print('3- Edit a contact \n')
    print('4- Dlete contacts\n')
    print('5- Exit\n')

    user_choice = input('\nEnter a choice number:  ')

    if not user_choice.isdigit() or len(user_choice) != 1 or user_choice == '0':

        print(f'Entry ({user_choice}) is not acceptable\nFollow the instructions please!\n')

    else:

        choice = int(user_choice)


        if choice == 1: # ADD A CONTACT

            add_data ()

        elif choice == 2: # View contacts

            if contacts:

                print("\n-------")

                for key in contacts:

                    print(key,': ', contacts[key])  

                print("\n-------")
                                
            else:
                print('\nThere is nothing to show!\nPlease add a contact!\n') 

        elif choice == 3 : # Edit a contact

            edit_data()

        elif choice == 4: # Delete contacts

            if contacts == {}: # check content

                print(f'\n--> Contact is already empty: {contacts}\n')

            else:

                contacts = {}

                print(f'\nContact is successfully deleted: ({contacts})\n')

        elif choice ==  5:

            game_on = False

        else:
            print(f"\nEntry ({user_choice}) out of range!\nPlease Enter a shoose of list\n ")


#Project [ UseCases ]

# CHECK IF KEYS ADDED IN DICTIONRAY TO SHOW SUCCES MASSEGE, AND SOLVING THE ERROR, THAT THE KEYS ARE NOT DEFINDE BECAUSE THEY NOT ALREADY ADDED [**Done**]

# WHEN I CHOICE 3- "EDIT_CONTACT" WHILE THE DICTIONRAY IS EMPTY I GOT KEYERROR 'USECASE': (**Done**)

# I WLOUD LIKE TO CHECK KEYS DICTIONRAY IF THEY FUL OR EMPTY: (**Done**)

# WHEN I CALL HERE CHOICES NUMBER 4 MAKE NOT BREAK OR FALSE: (**Done**)

# I WANAA PRINT DICTIONARY NAMES OF KEYS WITH (**DONE**)

# I SHOULD TO TEST IF USER INTERED CHARACTERS WITH NUMBER AND SOLVING THE ERROR: (**DONE**)



#***************(finished on 1 jun 2024)