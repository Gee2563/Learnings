from lib.user import User
from lib.post import Post
class UserRepo:
    def __init__(self,connection) -> None:
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM users')
        return [User(row['id'], row['email'],row['username']) for row in rows]
    
    def find(self,id):
        rows = self.connection.execute('SELECT * FROM users WHERE id = %s',[id])
        row = rows[0]
        return User(row['id'], row['email'],row['username'])
    
    def create(self,email,username):
        self.connection.execute('INSERT INTO users (email,username) VALUES (%s,%s)',[email,username])

    def delete(self,id):
        self.connection.execute('DELETE FROM users WHERE id = %s',[id])

    def find_with_posts(self,id):
        rows = self.connection.execute('''SELECT 
                                users.id AS user_id, 
                                users.email, 
                                users.username,
                                posts.id AS post_id,
                                posts.title,
                                posts.content,
                                posts.views
                                FROM users
                                JOIN posts ON users.id = posts.user_id
                                WHERE user_id = %s''',[id])
        posts = [Post(r['post_id'],r['title'],r['content'],r['views'],r['user_id']) for r in rows]

        return User(rows[0]['user_id'],rows[0]['email'],rows[0]['username'],posts)