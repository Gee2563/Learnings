from lib.dish import *

def test_dish_attributes():
    dish = Dish('Pad Thai', 10)
    assert dish.name == 'Pad Thai'
    assert dish.price == 10
    assert dish.available == True

def test_dish_out_of_stock():
    dish = Dish('won-ton', 10)
    dish.set_unavailable()
    assert dish.available == False
    