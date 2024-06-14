from lib.user_repo import UserRepo
from lib.user import User

def test_all(created_user_repo):
    assert created_user_repo.all() == [
        User(1,'user1','email1'),
        User(2,'user2','email2'),
        User(3,'user3','email3')
    ]

def test_find(created_user_repo):
    result = created_user_repo.find(1)
    assert result.username == 'user1'

def test_create(created_user_repo):
    created_user_repo.create('user4','email4')
    created_user_repo.create('user5','email5')
    assert created_user_repo.find(4).username == 'user4'

def test_delete(created_user_repo):
    created_user_repo.delete('user5')
    assert created_user_repo.all()[-1].username == 'user4'