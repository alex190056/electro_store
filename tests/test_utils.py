import pytest

from main import Item, Phone, KeyBoard


def test_calculate_total_price():
    item = Item("Ноутбук", 20000, 5)
    assert item.calculate_total_price() == 100000


def test_is_integer():
    assert Item.is_integer(5) is True
    assert Item.is_integer(5.0) is True
    assert Item.is_integer(5.5) is False


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

def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item = Item("iPhone 14", 120_000, 5)
    assert phone1 + item == 10

def test_KeyBoard():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert kb.language == 'EN'
    assert kb.change_lang() == 'RU'


def test_exception_long_name():
    """Проверка вызова исключения, если название товара будет превышать 10 символов"""
    item = Item(name='Iphone 10', price=60000, count=50)
    with pytest.raises(Exception):
        item.name = 'длинное название товара'

def test_attribute_number_of_sim():
    """
    Проверка того, что при инициализации объекта класса Phone
    нельзя задать атрибут number_of_sim <=0
    """
    phone = Phone(name='iPhone 10', price=60000, count=50, sims=2)
    with pytest.raises(ValueError):
        phone.number_of_sim = 0








