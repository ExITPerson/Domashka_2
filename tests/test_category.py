import pytest

from src.category import Category, Order
from src.product_iterator import ProductIterator
from src.products import Product
from src.smartphone_products import Smartphone


def test_category_farm(category_farm: Category) -> None:
    assert category_farm.name == "Farm fruits"
    assert category_farm.description == "Farm fruits"
    assert len(category_farm.products_in_list) == 3


def test_category_citrus(category_citrus: Category) -> None:
    assert category_citrus.name == "Citrus fruits"
    assert category_citrus.description == "Citrus fruits"
    assert len(category_citrus.products_in_list) == 4


def test_count_category_and_products() -> None:
    assert Category.category_count == 2
    assert Category.product_count == 7


def test_add_product_and_products() -> None:
    product1 = Product("Orange", "Krasnodar Orange", 50, 8)
    new_category = Category("Краснодарские фрукты", "Свежие фрукты из Краснодарского края", [product1])
    assert new_category.product_count == 8
    assert new_category.products == "Orange, 50 руб. Остаток: 8\n"
    product4 = Product("Ananas", "Krasnodar Ananas", 100, 7)
    new_category.add_product(product4)
    assert new_category.product_count == 9
    assert new_category.products == ("Orange, 50 руб. Остаток: 8\nAnanas, 100 руб. Остаток: 7\n")


def test_category_str(category: Category) -> None:
    assert str(category) == "Смартфоны, количество продуктов: 110"


def test_product_iterator(product_iterator: ProductIterator) -> None:
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Apple"
    assert next(product_iterator).name == "Grape"
    with pytest.raises(StopIteration):
        next(product_iterator)


def test_add_products_category(smartphone1: Smartphone, smartphone2: Smartphone) -> None:
    Category.product_count = 0
    category_smartphone = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    category_smartphone.add_product(smartphone3)
    assert Category.product_count == 3

    with pytest.raises(TypeError):
        category_smartphone.add_product("Новый продукт")


def test_order(product: Product):
    assert product.quantity == 10
    order = Order(product, 2)
    assert order.product.name == "Apple"
    assert order.order_count == 2
    assert order.total_price == 100.2
    assert order.print_count_products_in_stock() == 8
    assert product.quantity == 8

def test_category_print_count_products_in_stock(product, product2):
    Category.product_count = 0
    category = Category("Fruit", "New fruit", [product, product2])
    assert category.print_count_products_in_stock() == 110
    product3 = Product("Orange", "New orange", 23, 23)
    category.add_product(product3)
    assert category.print_count_products_in_stock() == 133

