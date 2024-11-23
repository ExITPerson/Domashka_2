from typing import Any

import pytest

from src.category import Category
from src.products import Product


@pytest.fixture
def product() -> Any:
    return Product("Apple", "Golden apple", 50.1, 10)


@pytest.fixture
def category_farm() -> Any:
    return Category("Farm fruits", "Farm fruits", ["Apple", "Pear", "Cherry"])


@pytest.fixture
def category_citrus() -> Any:
    return Category("Citrus fruits", "Citrus fruits", ["Orange", "Grape", "Limon", "Broomstick"])
