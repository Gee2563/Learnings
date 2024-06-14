from lib.entry import *
from lib.todo_list import *
import datetime
from dateutil.relativedelta import relativedelta




class Diary:
    def __init__(self):
        self.content = {}
        self.wpm = None
        self.today = datetime.datetime.now().date()
        self.today_str = self.today.strftime('%d-%m-%Y')
        self.test_date = datetime.date(2024,6,4)

    def set_content(self):
        # Check if the dictionary is empty
        end_date = self.today + relativedelta(years=2)

        current_date = self.today
        current_date_str = current_date.strftime('%d-%m-%Y')
    
        if not self.content:
            while current_date <= end_date:
                if current_date not in self.content:
                    self.content[current_date_str] = {
                        'Entries': [],
                        'Tasks': TodoList()
                    }
                current_date += datetime.timedelta(days=1)
    
    def extend_content(self):
        end_date = self.today + relativedelta(years=2)
        current_date = self.today

        while current_date <= end_date:
            date_str = current_date.strftime('%d-%m-%Y')

            if date_str not in self.content:
                self.content[date_str] = {
                    'Entries': [],
                    'Tasks': TodoList()
                }
            current_date += datetime.timedelta(days=1)

    def add_entry(self,entry:object):
        if isinstance(entry,Entry):
            self.content[self.today_str]['Entries'].append(entry.text)
        else:
            raise Exception('Wrong input')
    
    def add_task(self,todo:object):
        self.content[todo.datestring]['Tasks'].add_todo(todo)
    
