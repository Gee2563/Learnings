from lib.post import Post

class PostRepo:
    def __init__(self,connection) -> None:
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM posts')
        return [Post(row['id'],row['title'],row['content'],row['views'],row['user_id']) for row in rows]
    
    def find(self,id):
        rows = self.connection.execute('SELECT * FROM posts WHERE id = %s',[id])
        row = rows[0]
        return Post(row['id'],row['title'],row['content'],row['views'],row['user_id'])
    
    def create(self,title,content,views,user_id):
        self.connection.execute('INSERT INTO posts (title,content,views,user_id) VALUES (%s,%s,%s,%s)',[title,content,views,user_id])
    
    def delete(self,id):
        self.connection.execute('DELETE FROM posts WHERE id = %s',[id])