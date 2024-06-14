from lib.time_error import *
from unittest.mock  import Mock
import pytest

def test_error():
    requester_mock = Mock(name='requester')
    response_mock = Mock(name='response')

    requester_mock.get.return_value = response_mock

    response_mock.json.return_value = {
        'unixtime' : 1717495225
    }
    timer_mock  = Mock()
    timer_mock.time.return_value = 1717495233
    time_error = TimeError(requester_mock,timer_mock)
    
    result = time_error.error()
    assert result == -8
