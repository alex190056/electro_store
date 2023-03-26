import pytest

from main import Item, Phone, MixinKeyBoard


@pytest.fixture
def test_exception_long_name(item):
    """Проверка вызова исключения, если название товара будет превышать 10 символов"""
    with pytest.raises(Exception):
        item.name = 'длинное название товара'

def test_exception_file_not_found():
    """Проверка вызова исключения, если файл не найден"""
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(path='file.csv')  # напиши название файла, которого точно нет (например, file.csv, мы ожидаем файла item.csv, а не файла file.csv)

@pytest.fixture
def test_attribute_number_of_sim():
    """
    Проверка того, что при инициализации объекта класса Phone
    нельзя задать атрибут number_of_sim <=0
    """
    with pytest.raises(ValueError):
        Phone(name='iPhone 10', price=60000, count=50, sims=0)
