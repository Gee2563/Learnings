from lib.messaging import *
from unittest.mock import Mock
import pytest

def test_send_email(caplog):
    requester_mock = Mock(name='requester')
    response_mock = Mock(name='response')

    requester_mock.post.return_value = response_mock

    response_mock.status_code = 200
    
    messenger = Messaging(requester_mock)
    
    with caplog.at_level(logging.INFO):
        messenger.send_single_email('receiver123@received.com')
    
    assert "Successfully sent an email to 'receiver123@received.com' via Mailgun API." in caplog.text


    