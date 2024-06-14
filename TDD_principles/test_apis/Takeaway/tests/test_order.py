from lib.order import *
import pytest
from unittest.mock import Mock

@pytest.fixture
def created_order():
    order = Order()
    dish = Mock()
    dish.name = 'Pad Thai'
    dish.price = 10
    order.add_dish(dish)
    return order

def test_order_attributes():
    order = Order()
    assert order.list == []
    assert order.total_price == 0

def test_add_order(created_order):
    assert len(created_order.list) == 1
    assert created_order.total_price == 10

def test_remove_order(created_order):
    dish1 = Mock()
    dish1.name = 'Won-ton'
    dish1.price = 5
    created_order.add_dish(dish1)
    created_order.remove_dish(dish1)
    assert len(created_order.list) == 1

def test_view_order(created_order):
    assert created_order.view_order() == ['Pad Thai : 10']