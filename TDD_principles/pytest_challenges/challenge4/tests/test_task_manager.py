from lib.task_manager import *
import pytest

@pytest.fixture
def create_taskmgr():
    taskmgr = Taskmanager()
    taskmgr.add_task('Throw the bins out')
    taskmgr.add_task('Walk the dog')
    taskmgr.add_task('Swim the dolphin')
    return taskmgr

def test_invalid_task():
    with pytest.raises(Exception) as err:
        taskmgr = Taskmanager()
        taskmgr.add_task('')
    assert str(err.value) == 'Invalid input, please input a string.'

def test_empty_list_of_tasks():
    with pytest.raises(Exception) as err:
        taskmgr = Taskmanager()
        taskmgr.print_taks()
    assert str(err.value) == 'You tasklist is empty, please add a tasks to your list.'

def test_adding_task(create_taskmgr):
    assert create_taskmgr.tasks_list[-1] == 'Swim the dolphin'

def test_list_of_tasks(create_taskmgr):  
    assert create_taskmgr.print_taks() == 'Throw the bins out\nWalk the dog\nSwim the dolphin'

def test_checking_tasks_off(create_taskmgr):
    create_taskmgr.mark_complete(3)
    assert create_taskmgr.print_taks() == 'Throw the bins out\nWalk the dog'

def test_checking_tasks_off_invalid_input(create_taskmgr):
    with pytest.raises(Exception) as err:
        create_taskmgr.mark_complete('1')
    assert str(err.value) == 'Please input an integer.'

def test_checking_tasks_out_of_range(create_taskmgr):
    with pytest.raises(Exception) as err:
        create_taskmgr.mark_complete(4)
    assert str(err.value) == 'Please input an integer between 1 and 3.'

def test_removed_tasks(create_taskmgr):
    create_taskmgr.mark_complete(3)
    assert create_taskmgr.completed_tasks[-1] == 'Swim the dolphin'
    