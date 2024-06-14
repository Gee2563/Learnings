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

# Now, when we create a test, if we allow it to accept a parameter called `db_connection`,
# Pytest will automatically pass in the object we created above.

@pytest.fixture()
def created_user():
    user = User(1,'user1','email1')
    return user

# For example:

@pytest.fixture()
def created_post():
    post = Post(1,'Title1','This is content',100,1)
    return post

@pytest.fixture()
def created_user_repo():
    conn = DatabaseConnection()
    conn.connect()
    conn.seed("seeds/database_connection.sql")
    repo = UserRepo(conn)
    return repo

# def test_something(db_connection):
#     # db_connection is now available to us in this test.

@pytest.fixture()
def created_post_repo():
    conn = DatabaseConnection()
    conn.connect()
    conn.seed("seeds/database_connection.sql")
    repo = PostRepo(conn)
    return repo