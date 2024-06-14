from typing import Any


class Todo:
    
    def __init__(self,task):
        if type(task) == str and len(task) > 0:
            self.task = task
        else:
            raise Exception('Please input a string')
        
        self.complete = False

    
    def mark_complete(self):
        self.complete = True