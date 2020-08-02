__desc__ = "Auxiliary functions"
__author__ = "Filipe Ligeiro Silva"

from database_functions import database
from class_contact import contact

def print_contact(contact):
    if contact == "":
        print("{0:<25}\t{1:<15}\t{2:<40}".format("Name", "Number", "Email"))
        print("=" * (25 + 15 + 40))
    
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