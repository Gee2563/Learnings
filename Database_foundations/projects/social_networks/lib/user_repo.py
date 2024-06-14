from lib.user import User

class UserRepo:
    def __init__(self,connection) -> None:
        self.connection = connection
    
    def all(self):
        rows = self.connection.execute('SELECT * FROM users')
        return [User(row['id'], row['username'],row['email']) for row in rows]
    
    def find(self,user_id):
        rows = self.connection.execute('SELECT * FROM users WHERE id = %s',[user_id])
        row = rows[0]
        return User(row['id'], row['username'],row['email']) 
    
    def create(self,username,email):
        self.connection.execute('INSERT INTO users (username,email) VALUES (%s, %s)',[username,email])
    
    def delete(self, username):
        self.connection.execute('DELETE FROM users WHERE username = %s',[username])