__desc__ = "Command line contact book"
__author__ = "Filipe Ligeiro Silva"

def parser(contact):
    i = 0
    name = ""
    number = ""
    email = ""
    
    while contact[i] != ":":
        name += contact[i]
        i += 1

    i += 1
    while contact[i] != ":":
        number += contact[i]
        i += 1

    i += 1
    email = contact[i:]
    
    return name, number, email

def print_contact(contact):
    if contact == "":
        name = "Name"
        number = "Number"
        email = "Email"
    
    else:
        name, number, email = parser(contact)
    
    print("{0:<25}\t{1:<15}\t{2:<40}".format(name, number, email))

def query(string):
    choice = int(input(string))

    while choice not in range(1,7):
        print("Non existent option, please try again")
        choice = int(input(string))

    return choice

def find_contact(name):
    with open("data", "r") as file:
        contacts = file.readlines()
    
    i = 0
    for contact in contacts:
        if name in contact:
            return i, contact
        
        i += 1

    return -1, "" # not found

def add_contact(name, number, email):
    if find_contact(name)[0] != -1:
        print("ERROR: ALREADY EXISTING CONTACT")
        return
    
    add = name + ":" + number + ":" + email

    with open("data", "a") as file:
        file.write(add)

def remove_contact(index):
    if index == -1: #caso nao haja contacto para remover
        print("ERROR: NON EXISTING CONTACT")
        return
    
    with open("data", "r") as file:
        contacts = file.readlines()

    del(contacts[index])

    with open("data", "w") as file:
        file.writelines(contacts)

def edit_contact(index, contact):
    if index == -1: #caso nao haja contacto para editar
        print("ERROR: NON EXISTING CONTACT")
        return
    
    name, number, email = parser(contact)
    remove_contact(index)

    print("New data (press ENTER to not change something:")
    new_name = input("\tName: ")
    new_number = input("\tNumber: ")
    new_email = input("\tEmail: ")

    if new_name != "":
        name = new_name
    
    if new_number != "":
        number = new_number
    
    if new_email != "":
        email = new_email
    
    add_contact(name, number, email)

def list_contact(name):
    if find_contact(name)[0] != -1:
        print("ERROR: ALREADY EXISTING CONTACT")
        return
    
    _, contact = find_contact(name)

    print_contact("")

    print_contact(contact)

def list_all_contacts():
    with open("data", "r") as file:
        contacts = file.readlines()
    
    if contacts == []:
        print("NO CONTACTS")
        return

    print("{0:<25}\t{1:<15}\t{2:<40}\n".format("Name", "Number", "Email"))

    for contact in contacts:
        print_contact(contact)

if __name__ == "__main__":
    print("################################")
    print("# Welcome to your Contact Book #")
    print("################################")
    
    while True:
        print("\nPlease choose an option")
        print("\t1. Add contact\n\t2. Remove contact")
        print("\t3. Edit contact\n\t4. List a contact")
        print("\t5. List all contacts\n\t6. Exit")
        choice = query("")
        print("\n")
        
        if choice == 1:
            name = input("Name of the new contact: ")
            number = input("Number: ")
            email = input("Email: ")

            add_contact(name, number, email)
        
        elif choice == 2:
            name = input("Name of the contact to be removed: ")
            index, _ = find_contact(name)

            remove_contact(index)
        
        elif choice == 3:
            name = input("Name of the contact to be edited: ")
            index, contact = find_contact(name)

            edit_contact(index, contact)
        
        elif choice == 4:
            name = input("Name of the contact to be listed: ")
            list_contact(name)
        
        elif choice == 5:
            list_all_contacts()

        elif choice == 6:
            exit()     