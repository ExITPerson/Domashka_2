from src.category import Category
from src.products import Product


def test_category_farm(category_farm) -> None:
    assert category_farm.name == "Farm fruits"
    assert category_farm.description == "Farm fruits"
    assert len(category_farm.products_in_list) == 3


def test_category_citrus(category_citrus) -> None:
    assert category_citrus.name == "Citrus fruits"
    assert category_citrus.description == "Citrus fruits"
    assert len(category_citrus.products_in_list) == 4


def test_count_category_and_products() -> None:
    assert Category.category_count == 2
    assert Category.product_count == 7


def test_add_product_and_products():
    product1 = Product("Orange", "Krasnodar Orange", 50, 8)
    new_category = Category("Краснодарские фрукты", "Свежие фрукты из Краснодарского края", [product1])
    assert new_category.product_count == 8
    assert new_category.products == "Orange, 50 руб. Остаток: 8\n"
    product4 = Product("Ananas", "Krasnodar Ananas", 100, 7)
    new_category.add_product(product4)
    assert new_category.product_count == 9
    assert new_category.products == ("Orange, 50 руб. Остаток: 8\nAnanas, 100 руб. Остаток: 7\n")
