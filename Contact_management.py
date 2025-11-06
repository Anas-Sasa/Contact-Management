
# Contact Management [28 Mei 2024]
# Exercises: Dictionaries, Nested If Statements, Functions

# Initialize an empty dictionary to store contact information
contacts = {}

# Function to edit an existing contact
def edit_data():

    """
    Edits an existing contact in the contacts dictionary.

    Checks if the dictionary is empty before proceeding.
    Prompts the user to enter the contact ID, new name, and new phone number.
    Validates inputs and updates the contact if the ID matches.
    Displays appropriate messages for success or input errors.
    """

    # Check if the contacts dictionary is empty
    if contacts == {}:
        print('\nContacts is empty there is nothing to edit:\nPlease add a contact:\n')

    else:
        print('\nEdit a contact:\n_____\n')

        # Ask user for the contact ID to edit
        contact_id = input('\nEnter the contact [id]:  ')

        # Ask user for the contact ID to edit
        if contact_id.isdigit():

            # Verify if the entered ID matches the stored contact ID
            if  contact_id != contacts['user_id']:
                print(f'\nID number ({contact_id}) is not exist:\n')

            else:  

                # Ask for new name and format it
                edit_name = input("\nEnter the contact new name:  ").title()

                # Ensure name is not empty
                if len(edit_name) >=1:

                    # Ask for new phone number
                    edit_phone_num = input('\nEnter a new phone number:  ')

                    # Validate phone number is numeric
                    if edit_phone_num.isdigit(): 

                        # Update contact details
                        contacts['phone'] = edit_phone_num
                        contacts['name'] = edit_name

                    else:
                        print(f'\nYour input phone ({edit_phone_num}) not a digit:\n')
                   
                    # Confirm if both fields were updated correctly
                    if edit_name == contacts['name'] and edit_phone_num == contacts['phone']:
                        
                        print('\nEdits was successfully!\nYou can check your new contact!\n\n')
        
                    else:
                        print(f"Please enter the required data:\nTry after 2 minutes")

                else:
                    print('\nYou did not enter a name!\n\n')

        else:
            print(f'Your input ({contact_id}) is not a digit:\nWe accepte only digits. Try again!')
  

# Function to add a new contact
def add_data():

    """
    Adds a new contact to the contacts dictionary.

    Prompts the user to enter a name, phone number, and ID.
    Validates each input and stores the contact if all inputs are valid.
    Displays a success or error message based on the result.
    """

    print('\n\nAdd a contact;\n_____\n')

    # Ask for name and format it
    name = input("\nEnter name:  ").title()

    # Validate name contains only letters
    if name.isalpha():

        phone_num = (input("\nEnter a phone number:  "))

        # Validate phone number is numeric
        if phone_num.isdigit():

            id = (input('\nEnter an ID of contact:  '))
            
            # Validate ID is numeric
            if id.isdigit():

                # Store contact details in dictionary
                contacts['name'] = name
                contacts['phone'] = phone_num
                contacts['user_id'] = id 

            else:
                    print(f"Id [{id}] is not acceptable!\n\n")

        else:
            print(f'Phone number ({phone_num}) is not acceptable!\nTry again:\n ')

        # Confirm if all three fields were added
        if len(contacts) == 3:
                print('\nAdd was successfully\n')
        else:
            print('\nAdd was not seccfully:\nTry again:\n') 

    else:
            print(f'Entry [ {name} ] is not acceptable!\nYou only can enter characters!\n')

# Main loop to run the contact management system
game_on = True

while game_on:

    # Display menu options
    print("\n\nContact Management;\n_____\n")
    print('1- Add a contact\n')
    print('2- View contacts\n')
    print('3- Edit a contact \n')
    print('4- Dlete contacts\n')
    print('5- Exit\n')

    # Get user choice
    user_choice = input('\nEnter a choice number:  ')

    # Validate input is a single digit and not zero
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

            if contacts == {}: # Check content

                print(f'\n--> Contact is already empty: {contacts}\n')

            else:

                contacts = {}

                print(f'\nContact is successfully deleted: ({contacts})\n')

        elif choice ==  5: # Exit the program

            game_on = False

        # Handle invalid menu choices
        else:
            print(f"\nEntry ({user_choice}) out of range!\nPlease Enter a shoose of list\n ")



# Project Use Cases (documented issues and fixes)

# - Checked if keys are added before accessing them [**Done**]
# - Handled KeyError when editing empty dictionary [**Done**]
# - Verified dictionary content before operations [**Done**]
# - Ensured delete option resets dictionary without crashing [**Done**]
# - Printed dictionary keys and values clearly [**Done**]
# - Validated user input for characters and digits [**Done**]

# *************** (finished on 1 jun 2024)