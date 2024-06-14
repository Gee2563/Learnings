from lib.recipe import Recipe
import pytest

@pytest.fixture
def created_recipe():
    recipe = Recipe(1,'Pad Thai',30, 5)
    return recipe

def test_recipe_attributes(created_recipe):
    assert created_recipe.name == 'Pad Thai'
    assert created_recipe.cooking_time == 30
    assert created_recipe.rating == 5

def test_format_looks_good(created_recipe):
    assert str(created_recipe) == 'Recipe(1, Pad Thai, 30, 5)'

def test_is_it_the_same(created_recipe):
    recipe2 = Recipe(1,'Pad Thai',30, 5)
    assert recipe2 == created_recipe