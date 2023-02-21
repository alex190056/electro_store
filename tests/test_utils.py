from main import Item


def test_calculate_total_price():
    item = Item("Ноутбук", 20000, 5)
    assert item.get_total_price() == 100000


def test_is_integer():
    assert Item.is_integer(5) == True
    assert Item.is_integer(5.0) == True
    assert Item.is_integer(5.5) == False
