__desc__ = "Translators between contact and text"
__author__ = "Filipe Ligeiro Silva"

from class_contact import contact

def text_to_contact(text):
    i = 0
    name = ""
    number = ""
    email = ""
    
    while text[i] != ":":
        name += text[i]
        i += 1

    i += 1
    while text[i] != ":":
        number += text[i]
        i += 1

    i += 1
    email = text[i:-1]
    
    return name, number, email

def contact_to_text(contact):
    return contact.name + ":" + contact.number + ":" + contact.email + "\n"