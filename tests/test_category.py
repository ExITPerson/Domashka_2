from src.category import Category


def test_category_farm(category_farm):
    assert category_farm.name == "Farm fruits"
    assert category_farm.description == "Farm fruits"
    assert len(category_farm.products) == 3


def test_category_citrus(category_citrus):
    assert category_citrus.name == "Citrus fruits"
    assert category_citrus.description == "Citrus fruits"
    assert len(category_citrus.products) == 4


def test_count_category_and_products():
    assert Category.category_count == 2
    assert Category.product_count == 7
