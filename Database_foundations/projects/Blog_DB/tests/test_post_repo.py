from lib.post import Post
from lib.post_repo import *

def test_all_function(created_post_repo):
    assert created_post_repo.all() == [
        Post(1,'title1','content1',10,1),
        Post(2,'title2','content2',20,2),
        Post(3,'title3','content3',30,1),
        Post(4,'title4','content4',100,3),
        Post(5,'title5','content5',4000,1)

    ]

def test_find(created_post_repo):
    assert created_post_repo.find(1) == Post(1,'title1','content1',10,1)

def test_create(created_post_repo):
    created_post_repo.create('title6','content6',30,2)
    assert created_post_repo.find(6) == Post(6,'title6','content6',30,2)

def test_delete(created_post_repo):
    created_post_repo.delete(2)
    assert created_post_repo.all() == [
        Post(1,'title1','content1',10,1),
        Post(3,'title3','content3',30,1),
        Post(4,'title4','content4',100,3),
        Post(5,'title5','content5',4000,1)

    ]

def test_find_by_tag(created_post_repo):
    