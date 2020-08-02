__desc__ = "Class \"Contact\" for the Contact Book "
__author__ = "Filipe Ligeiro Silva"

class contact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email

    def get_name(self):
        return self.name
    
    def get_number(self):
        return self.number
    
    def get_email(self):
        return self.email

    def change_name(self, new):
        if new == "":
            return
        
        self.name = new
    
    def change_number(self, new):
        if new == "":
            return
        
        self.number = new
    
    def change_email(self, new):
        if new == "":
            return
        
        self.email = new

    def __repr__(self):
        return("{0:<25}\t{1:<15}\t{2:<40}"\
            .format(self.name, self.number, self.email))