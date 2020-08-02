__desc__ = "Database functions"
__author__ = "Filipe Ligeiro Silva"

database = []

from translators import text_to_contact, contact_to_text
from class_contact import contact

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