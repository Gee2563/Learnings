class Taskmanager:
    def __init__(self):
        self.tasks_list = []
        self.completed_tasks = []
    
    def add_task(self,task):
        if type(task) != str or len(task) == 0:
            raise Exception('Invalid input, please input a string.')
        else:
            self.tasks_list.append(task)

    def print_taks(self):
        if len(self.tasks_list) == 0:
            raise Exception('You tasklist is empty, please add a tasks to your list.')
        else:
            return ('\n').join([task for task in self.tasks_list])
        
    def mark_complete(self, index):
        if type(index) != int:
            raise Exception('Please input an integer.')
        if index < 1 or index > len(self.tasks_list):
            raise Exception(f'Please input an integer between 1 and {len(self.tasks_list)}.')
        else:
            self.completed_tasks.append(self.tasks_list.pop(index-1))
    
