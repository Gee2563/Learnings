from lib.recipe import Recipe

class RecipeRepo:
    def __init__(self,connection) -> None:
        self.connection = connection
    
    def all(self):
        rows = self.connection.execute('SELECT * from recipes')
        return [ Recipe(row["id"], row["name"], row["cooking_time"], row['rating']) for row in rows]
    
    def find(self,id):
        rows = self.connection.execute('SELECT * FROM recipes WHERE id = %s',[id])
        row = rows[0]
        return Recipe(row["id"], row["name"], row["cooking_time"], row['rating'])