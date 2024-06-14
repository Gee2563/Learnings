

from datetime import datetime

class PasswordManager2:
    def __init__(self) -> None:
        self.info = []
        self.allpassword =[]
        self.allservices = []
    
    def password_validator(self,password:str):
        specials = '!@$%&'
        if len(password) > 7 and password not in self.allpassword:
            for char in specials:
                if char in password:
                    return True
        return False

    def add(self, servName: str, password: str):
        if self.password_validator(password) == True and servName not in self.allservices:
            self.info.append({'name': servName, 'password': password, 'time': datetime.now()})
            self.allpassword.append(password)
            self.allservices.append(servName)
    
    def remove(self, servName):
        #remove dictionary from the list self.info
        placeholder = [ dictionary for dictionary in self.info if dictionary['name'] != servName]
        self.info = placeholder

    def update(self, servName:str,password:str):
        #check password is valid
        if self.password_validator(password) == True:
            for dictionary in self.info:
                if dictionary['name'] == servName:
                    old_password = dictionary['password']
                    self.allpassword.remove(old_password)
                    dictionary['password'] = password
                    self.allpassword.append(password)

    #search for dictionary[servName] and update the password -for dictionary in self.info ... dictionary[password] = new password
        
    def list_services(self):
        #return a list of only servName
        return [dictionary['name'] for dictionary in self.info]

    def sort_services_by(self,command, reverse=None):
        if command == 'service':
            array = sorted(self.list_services())
        if command == 'added_on':
            array = [tuples[1] for tuples in sorted([(dictionary['time'],dictionary['name']) for dictionary in self.info])]
        if reverse is not None:
                array = array[::-1]
        return array
        #condition 1 : string or added on?
        #condition 2 : is args[1] == reverse?
        #if string --> return a list in a sorted order by either ascending or descending based on condition2
        
    def get_for_service(self, servName):
        for dictionary in self.info:
            if dictionary['name'] == servName:
                return dictionary['password']
        #return the password for the servName

