from lib.user import *

def test_user_attributes(created_user):
    assert created_user.id == 1
    assert created_user.email =='email1'

def test_string_format(created_user):
    assert str(created_user) == 'User(1, email1, usernam1, [])'

def test_is_equal_to(created_user):
    user1 = User(1,'email1','usernam1')
    assert user1 == created_user