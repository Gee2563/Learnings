from lib.recipes_repo import RecipeRepo
from lib.recipe import Recipe
import pytest

def test_get_all_records(db_connection):
    db_connection.seed('seeds/recipes.sql')
    repo = RecipeRepo(db_connection)
    recipes = repo.all()
    assert recipes == [
        Recipe(1,'Pad Thai', 30, 5),
        Recipe(2,'Spaghetti Carbonara', 30, 5),
        Recipe(3,'Roast Duck', 150, 4),
        Recipe(4,'Burger and Lobster', 50, 5),
        Recipe(5,'Boiled Potato', 10, 2)
    ]

def test_find_single_record(db_connection):
    db_connection.seed('seeds/recipes.sql')
    repo = RecipeRepo(db_connection)
    recipe = repo.find(3)
    assert recipe == Recipe(3,'Roast Duck', 150, 4)