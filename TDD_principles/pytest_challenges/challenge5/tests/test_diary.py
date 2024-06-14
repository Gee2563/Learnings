# from lib.diary import *
# from lib.entry import *
# from lib.todo_list import *
# import pytest

# @pytest.fixture
# def create_diary():
#     diary = Diary()
#     diary.set_content()
#     diary.extend_content()
#     diary.add_entry(Entry('I walked the dog today'))
#     diary.add_task(Todo('Wish mum happy birthday', '04-06-2024'))
#     return diary

# def test_diary_init(create_diary):
#     assert type(create_diary.content) == dict
#     # My diary will be formatted as a dictionary - the keys will be the date, the first key is today the last key is end of year 2026
#     assert len(create_diary.content.keys()) == 731

#     # I want to add new tasks and entries based on date.
# def test_add_entries(create_diary):
#     assert create_diary.content['31-05-2024']['Entries'][0] == 'I walked the dog today'
#     with pytest.raises(Exception) as err:
#         create_diary.add_entry(Diary())
#     assert str(err.value) == 'Wrong input'
#     # I want to add tasks
# def test_add_task(create_diary):
#     assert create_diary.content['04-06-2024']['Tasks'].print_list() == '04-06-2024 : Wish mum happy birthday'
#     # I want to check timenow and import any overdue tasks to timenow

# def test_date_and_overdue_tasks():
#     diary = Diary()
#     todolist = TodoList()
#     todolist.list = ['Throw the rubbish out']
#     diary.content['30-05-2024'] = {'Tasks': todolist }
#     assert diary.content['30-05-2024']['Tasks'].print_list() == '30-05-2024 : Throw the rubbish out'

#     # I want to receive a list of entries based on my wpm - which I can set globally.

