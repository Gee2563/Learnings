from lib.user import *

def test_user_inits(created_user):
    assert created_user.username == 'user1'
    assert created_user.email == 'email1'

def test_user_formats_well(created_user):
    assert str(created_user) == 'User(1, user1, email1)'

def test_is_equal(created_user):
    user = User(1,'user1','email1')
    assert created_user == user