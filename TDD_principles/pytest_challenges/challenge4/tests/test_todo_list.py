from lib.todo_list import *
from lib.todo import *
import pytest

@pytest.fixture
def create_todo():
    todo = Todo('walk the dog')
    todo.mark_complete()
    return todo

def test_todo_init(create_todo):
    with pytest.raises(Exception) as err:
        Todo(123)
    assert str(err.value) == 'Please input a string'
    assert create_todo.task == 'walk the dog'
    result  = Todo('Swim the dolphin')
    assert result.complete == False

def mark_complete(create_todo):
    assert create_todo.complete == True