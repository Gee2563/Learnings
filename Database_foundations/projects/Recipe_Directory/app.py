from lib.recipes_repo import RecipeRepo
from lib.database_connection import DatabaseConnection


connection = DatabaseConnection()
connection.connect()

connection.seed('seeds/recipes.sql')
repo= RecipeRepo(connection)

recipes = repo.all()

for recipe in recipes:
    print(recipe)