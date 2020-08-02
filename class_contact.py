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
        name_pad = 30
        number_pad = 15
        email_pad = 40

        ret = "{:<{x}}\t{:<{y}}\t{:<{z}}".format(self.name, self.number,\
            self.email, x = name_pad, y = number_pad, z = email_pad)
        
        if self.name == "Name" and self.number == "Number"\
            and self.email == "Email":

            ret += "\n" + "=" * (name_pad + number_pad + email_pad)
        
        return ret
