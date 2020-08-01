__desc__ = "Command line contact book"
__author__ = "Filipe Ligeiro Silva"

from translators import *

database = []

def load_db():
    with open("data") as file:
        text = file.readlines()
    
    for el in text:
        name, number, email = text_to_contact(el)
        
        database.append(contact(name, number, email))

def save_db():
    with open("data", "w") as file:
        for el in database:
            add = contact_to_text(el)

            file.write(add)

def print_contact(contact):
    if contact == "":
        print("{0:<25}\t{1:<15}\t{2:<40}".format("Name", "Number", "Email"))
    
    else:
        print(contact)

def query(string, inicial, final):
    choice = int(input(string))

    while choice not in range(inicial, final + 1):
        print("Non existent option, please try again")
        choice = int(input(string))

    return choice

def find_contact(name):
    i = 0
    for contact in database:
        if name in contact.get_name():
            return i # index of the contact in the list
        
        i += 1

    return -1, "" # not found

def add_contact(name, number, email):
    if find_contact(name) != -1:
        print("ERROR: ALREADY EXISTING CONTACT")
        return
    
    new = contact(name, number, email)

    database.append(new)

def remove_contact(index):
    index = find_contact(name)

    if index == -1:
        print("ERROR: NON EXISTING CONTACT")
        return

    del(database[index])

def edit_contact(name):
    index = find_contact(name)

    if index == -1:
        print("ERROR: NON EXISTING CONTACT")
        return


    print("New data (press ENTER to not change something:")
    new_name = input("\tName: ")
    new_number = input("\tNumber: ")
    new_email = input("\tEmail: ")

    database[index].change_name(new_name)
    database[index].change_number(new_number)
    database[index].change_email(new_email)

def list_contact(name):
    index = find_contact(name)

    if index == -1:
        print("ERROR: NON EXISTING CONTACT")
        return

    print_contact("")

    print_contact(database[index])

def list_all_contacts():
    if database == []:
        print("NO CONTACTS")
        return

    print_contact("")

    for contact in database:
        print_contact(contact)

if __name__ == "__main__":
    load_db()

    print("################################")
    print("# Welcome to your Contact Book #")
    print("################################")
    
    while True:
        print("\nPlease choose an option")
        print("\t1. Add contact\n\t2. Remove contact")
        print("\t3. Edit contact\n\t4. List a contact")
        print("\t5. List all contacts\n\t6. Exit")
        choice = query("", 1, 6)
        print("\n")
        
        if choice == 1:
            name = input("Name of the new contact: ")
            number = input("Number: ")
            email = input("Email: ")

            add_contact(name, number, email)
        
        elif choice == 2:
            name = input("Name of the contact to be removed: ")
            remove_contact(name)
        
        elif choice == 3:
            name = input("Name of the contact to be edited: ")
            edit_contact(name)
        
        elif choice == 4:
            name = input("Name of the contact to be listed: ")
            list_contact(name)
        
        elif choice == 5:
            list_all_contacts()

        elif choice == 6:
            question = "Do you wish to save the changes made?\
                \n\t1. Yes\n\t2. No\n"

            choice = query(question, 1, 2)

            if choice == 1:
                save_db()

            exit()     