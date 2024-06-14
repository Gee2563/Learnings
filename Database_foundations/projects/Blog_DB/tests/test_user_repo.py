from lib.user_repo import *
from lib.user import User
from lib.post import Post

def test_all_function(created_user_repo):
    assert created_user_repo.all() == [
        User(1,'email1','username1'),
        User(2,'email2','username2'),
        User(3,'email3','username3')
    ]

def test_find_function(created_user_repo):
    assert created_user_repo.find(1) == User(1,'email1','username1')


def test_create_function(created_user_repo):
    created_user_repo.create('email4','username4')
    assert created_user_repo.find(4) == User(4,'email4','username4')

def test_delete_function(created_user_repo):
    created_user_repo.delete(3)
    assert created_user_repo.all() == [
        User(1,'email1','username1'),
        User(2,'email2','username2')
    ]

def test_find_with_posts(created_user_repo):
    user = created_user_repo.find_with_posts(1)
    user1 = User(1,'email1','username1',[
        Post(1,'title1','content1',10,1),
        Post(3,'title3','content3',30,1),
        Post(5,'title5','content5',4000,1)
    ])
    assert user == user1
