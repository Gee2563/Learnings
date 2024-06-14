from lib.post import *

def test_attributes(created_post):
    assert created_post.id == 1
    assert created_post.title == 'title1'


def test_format(created_post):
    assert str(created_post) == 'Post(1, title1, This is content, 10, 1)'

def test_is_equal(created_post):
    post = Post(1,'title1','This is content',10,1)
    assert post == created_post