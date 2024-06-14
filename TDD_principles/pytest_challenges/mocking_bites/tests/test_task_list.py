from lib.task_list import TaskList
from unittest.mock import Mock


def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

# Unit test `#tasks` and `#all_complete` behaviour

def test_add_fake_taks():
    task_list = TaskList()
    fake_task1 = Mock()
    fake_task1.name = 'Walk the dog.'
    fake_task1.complete = False
    task_list.add(fake_task1)
    assert task_list.tasks[0].name == 'Walk the dog.'