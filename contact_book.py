__desc__ = "Command line contact book"
__author__ = "Filipe Ligeiro Silva"

import argparse
from auxiliary_functions import query
from database_functions import save_db, load_db
from main_functions import add_contact, remove_contact, edit_contact,\
    list_contact, list_all_contacts

def verbose_mode():
    print("################################")
    print("# Welcome to your Contact Book #")
    print("################################")
    
    while True:
        print("\nPlease choose an option")
        print("\t1. Add contact\n\t2. Remove contact")
        print("\t3. Edit contact\n\t4. List a contact")
        print("\t5. List all contacts\n\t6. Exit")

        choice = query("", 1, 6)
        print("")

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
            print("")
            list_contact(name)
        
        elif choice == 5:
            list_all_contacts()

        elif choice == 6:
            question = "Do you wish to save the changes made?\
                \n\t1. Yes\n\t2. No\n"

            choice = query(question, 1, 2)

            if choice == 2:
                exit()

            return

if __name__ == "__main__":
    load_db()

    help = "Check the README.md file"
    parser = argparse.ArgumentParser(description=help)
    functions = parser.add_mutually_exclusive_group()

    functions.add_argument("-v", "--verbose", action="store_true")
    functions.add_argument("-a", "--add", action="store_true")
    functions.add_argument("-r", "--remove", action="store_true")
    functions.add_argument("-e", "--edit", action="store_true")
    functions.add_argument("-l", "--list", action="store_true")
    functions.add_argument("-la", "--listall", action="store_true")

    parser.add_argument("-n", "--name", dest="name", action="store")
    parser.add_argument("-p", "--phone", dest="phone", action="store")
    parser.add_argument("-m", "--email", dest="email" ,action="store")

    args = parser.parse_args()

    if args.verbose:
        verbose_mode()
    
    elif args.add:
        add_contact(args.name, args.phone, args.email)
    
    elif args.remove:
        remove_contact(args.name)

    elif args.edit:
        edit_contact(args.name)
    
    elif args.list:
        list_contact(args.name)
    
    elif args.listall:
        list_all_contacts()
    
    save_db()