import pytest
from main import Item

def test_get_total_price():
    item1 = Item('Смартфон', 10000, 20)
    item2 = Item('Ноутбук', 20000, 5)
    assert item1.get_total_price() == 200000
    assert item2.get_total_price() == 100000

def test_apply_discount():
    item1 = Item('Смартфон', 10000, 20)
    item2 = Item('Ноутбук', 20000, 5)
    assert item1.apply_discount() == 160000
    assert item2.apply_discount() == 80000
