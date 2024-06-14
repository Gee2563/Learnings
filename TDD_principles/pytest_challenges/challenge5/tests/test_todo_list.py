# from  lib.task import *
# import pytest 


# @pytest.fixture
# def create_todo():
#     todo = Todo('Swim the dolphin', '04-06-2024')
#     return todo

#  # check the object has been added

# def test_todo_format(create_todo):
#     assert create_todo.format() == '04-06-2024 : Swim the dolphin'


# def test_todo_init(create_todo):
#     assert create_todo.text == 'Swim the dolphin'
#     assert create_todo.date == datetime.datetime(2024,6,4)

#     with pytest.raises(Exception) as err:
#         todo1 = Todo(1, '04/06/2024')
#         todo2 = Todo('Swim the dolphin', 1)
#         todo3 = Todo('Swim the dolphin', '04-06/2022')
#     assert str(err.value) == 'Invalid format'

# # I want my to do list to include text attribute and completion date 
