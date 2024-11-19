import pytest

from src.category import Category
from src.products import Product


@pytest.fixture
def product():
    return Product("Apple", "Golden apple", 50.1, 10)


@pytest.fixture
def category_farm():
    return Category("Farm fruits", "Farm fruits", ["Apple", "Pear", "Cherry"])


@pytest.fixture
def category_citrus():
    return Category(
        "Citrus fruits", "Citrus fruits", ["Orange", "Grape", "Limon", "Broomstick"]
    )
