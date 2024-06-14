import datetime

class Todo:
    def __init__(self,text,date_string):
        if type(text) == str and len(text) > 2 and type(date_string) == str and len(date_string) == 10:
            self.text = text
            self.set_date(date_string)
            self.datestring = date_string
        else:
            raise Exception('Invalid format')
        
    def set_date(self,date_string):
        try:
            datetime_object = datetime.datetime.strptime(date_string, '%d-%m-%Y')
            if datetime_object > datetime.datetime.now():
                self.date = datetime_object
                self.datestring = date_string
            else:
                raise Exception('Invalid format')
        
        except ValueError:
            raise Exception('Invalid format')
        
