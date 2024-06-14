from lib.taskformatter import *
import pytest
from unittest.mock import Mock

def test_task_format():
    # ensure the taskformatter only accepts class task?
    fake_task = Mock()
    fake_task.title = 'Walk the dog.'
    fake_task.complete = False
    task_formatter = TaskFormatter(fake_task)
    assert task_formatter.task == fake_task
    assert task_formatter.format() == '- [ ] Walk the dog.'
    