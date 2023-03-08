import pytest

from main import Item, Phone


def test_calculate_total_price():
    item = Item("Ноутбук", 20000, 5)
    assert item.calculate_total_price() == 100000


def test_is_integer():
    assert Item.is_integer(5) is True
    assert Item.is_integer(5.0) is True
    assert Item.is_integer(5.5) is False



def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item = Item("iPhone 14", 120_000, 5)
    assert phone1 + item == 10


def test__repr__():
    item = Item("Ноутбук", 20000, 5)
    assert item.__repr__() != Item("Смартфон", '10000', '20')

def test__str__():
    item = Item("Ноутбук", 20000, 5)
    assert item.__str__() != Item("Смартфон", '10000', '20')

def test__init_phone__():
    phone1 = Phone('Iphone 14', 120_000, 5, 2)
    assert phone1.name == 'Iphone 14'
    assert phone1.price == 120_000
    assert phone1.count == 5
