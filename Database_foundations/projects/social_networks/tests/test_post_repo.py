from lib.post_repo import PostRepo
from lib.post import Post

def test_all_function(created_post_repo):
    assert created_post_repo.all() == [
        Post(1,'title1','this is content',10,1),
        Post(2,'title2','this is content',20,2),
        Post(3,'title3','this is content',300,1)
    ]

def test_find_function(created_post_repo):
    assert created_post_repo.find(1) == Post(1,'title1','this is content',10,1)


def test_create_function(created_post_repo):
    created_post_repo.create('title4','this is content',4000,3)
    assert created_post_repo.find(4) == Post(4,'title4','this is content',4000,3)

def test_delecte_function(created_post_repo):
    created_post_repo.delete(4)
    assert created_post_repo.all() == [
        Post(1,'title1','this is content',10,1),
        Post(2,'title2','this is content',20,2),
        Post(3,'title3','this is content',300,1)
    ]