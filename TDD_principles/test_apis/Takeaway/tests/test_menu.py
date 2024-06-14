from lib.menu import *
from unittest.mock import Mock
import pytest

@pytest.fixture
def created_menu():
    menu = Menu()
    dish1 = Mock()
    dish1.name = 'Pad Thai'
    dish1.price = 10
    dish1.available = True
    menu.add_dish(dish1)

    dish = Mock()
    dish.name = 'Won-Ton'
    dish.price = 5
    dish.available = False
    menu.add_dish(dish)

    return menu


def test_menu_attributes():
    menu = Menu()
    assert menu.list == []

def test_add_dish(created_menu):
    assert len(created_menu.list) == 2

def test_show_available_dishes(created_menu):
    assert created_menu.show_available_dishes() == ['Pad Thai : 10']