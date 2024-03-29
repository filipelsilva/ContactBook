__desc__ = "Main functions"
__author__ = "Filipe Ligeiro Silva"

from auxiliary_functions import find_contact, print_contact
from database_functions import database
from class_contact import contact

def add_contact(name, number, email):
    if name.strip() == "" or number.strip() == "" or email.strip() == "":
        print("ERROR: Invalid value or values, do not leave spaces empty")
        return
    
    index = find_contact(name)

    if index != -1 and database[index].get_name() == name:
        print("ERROR: ALREADY EXISTING CONTACT")
        return
    
    new = contact(name, number, email)

    database.append(new)

def remove_contact(name):
    if name.strip() == "":
        print("ERROR: Invalid value, do not leave spaces empty")
        return
    
    index = find_contact(name)

    if index == -1:
        print("ERROR: NON EXISTING CONTACT")
        return

    del(database[index])

def edit_contact(name):
    if name.strip() == "":
        print("ERROR: Invalid value, do not leave spaces empty")
        return
    
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
    if name.strip() == "":
        print("ERROR: Invalid value, do not leave spaces empty")
        return
    
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