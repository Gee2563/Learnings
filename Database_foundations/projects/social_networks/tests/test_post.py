from lib.post import *

def test_post_inits(created_post):
    assert created_post.id == 1
    assert created_post.title == 'Title1'
    assert created_post.content == 'This is content'
    assert created_post.views == 100
    assert created_post.user_id == 1


def test_post_formats_well(created_post):
    assert str(created_post) == 'Post(1, Title1, This is content, 100, 1)'

def test_is_equal(created_post):
    post = Post(1,'Title1','This is content',100,1)
    assert created_post == post