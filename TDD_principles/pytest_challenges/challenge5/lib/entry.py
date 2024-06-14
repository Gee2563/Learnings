import phonenumbers

class Entry:
    def __init__(self,text):
        self.text = text
        if type(text) == str and len(text) >=5:
            self.text = text
        else:
            raise Exception('Invalid input')
        self.reading_time = None
        self.contact_infos = {}
    
    def set_reading_time(self,wpm):
        if type(wpm) == int:
            self.reading_time = len(self.text.split(' ')) / wpm
        else:
            raise Exception('Invalid wpm')
        
    def check_and_return_contact_info(self):
        names = list(set(name[1:] for name in self.text.split(' ') if name.startswith('#') and name != '#TODO'))
        phone_numbers = [phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164) for match in phonenumbers.PhoneNumberMatcher(self.text, 'GB')]

        # Creating a dict to associate names with numbers
        if len(names) > len(phone_numbers):
            raise ValueError('Too many names.')
        else:
            for name, number in zip(names, phone_numbers):
                self.contact_infos[name] = number

            # Handle any remaining numbers if they exist
            remaining_numbers = phone_numbers[len(names):]

            if remaining_numbers:
                self.contact_infos["Additional"] = remaining_numbers

        
        return self.contact_infos