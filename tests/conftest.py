from typing import Any

import pytest

from src.category import Category
from src.product_iterator import ProductIterator
from src.products import Product


@pytest.fixture
def product() -> Any:
    return Product("Apple", "Golden apple", 50.1, 10)


@pytest.fixture
def product2() -> Any:
    return Product("Grape", "Krasnodar grape", 60.1, 100)


@pytest.fixture
def product_iterator(category):
    return ProductIterator(category)


@pytest.fixture
def category_farm() -> Any:
    return Category("Farm fruits", "Farm fruits", ["Apple", "Pear", "Cherry"])


@pytest.fixture
def category_citrus() -> Any:
    return Category("Citrus fruits", "Citrus fruits", ["Orange", "Grape", "Limon", "Broomstick"])


@pytest.fixture
def category(product, product2):
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product, product2]
    )
    return category1
