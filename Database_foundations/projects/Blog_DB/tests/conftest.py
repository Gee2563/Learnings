import pytest
from lib.database_connection import DatabaseConnection
from lib.user import User
from lib.post import Post
from lib.user_repo import UserRepo
from lib.post_repo import PostRepo

# This is a Pytest fixture.
# It creates an object that we can use in our tests.
# We will use it to create a database connection.
@pytest.fixture
def db_connection():
    conn = DatabaseConnection()
    conn.connect()
    return conn

@pytest.fixture
def created_user():
    user = User(1,'email1','usernam1')
    return user

@pytest.fixture
def created_post():
    post =  Post(1,'title1','This is content',10,1)
    return post

@pytest.fixture
def created_user_repo():
    conn = DatabaseConnection()
    conn.connect()
    conn.seed('seeds/blogging_app.sql')
    user_repo = UserRepo(conn)

    return user_repo

@pytest.fixture
def created_post_repo():
    conn = DatabaseConnection()
    conn.connect()
    conn.seed('seeds/blogging_app.sql')
    post_repo = PostRepo(conn)

    return post_repo


    
# Now, when we create a test, if we allow it to accept a parameter called `db_connection`,
# Pytest will automatically pass in the object we created above.

# For example:

# def test_something(db_connection):
#     # db_connection is now available to us in this test.
