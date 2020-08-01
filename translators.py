__desc__ = "Translators between contact and text for the Contact Book "
__author__ = "Filipe Ligeiro Silva"

from contact import contact

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
    email = text[i:]
    
    return name, number, email

def contact_to_text(contact):
    return contact.name + ":" + contact.number + ":" + contact.email