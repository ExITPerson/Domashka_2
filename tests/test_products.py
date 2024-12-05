from unittest.mock import patch

import pytest

from src.product_iterator import ProductIterator
from src.products import Product


def test_product(product) -> None:
    assert product.name == "Apple"
    assert product.description == "Golden apple"
    assert product.price == 50.1
    assert product.quantity == 10


def test_new_product():
    new_product = Product.new_product(
        {"name": "Orange", "description": "Krasnodar Orange", "price": 50.1, "quantity": 10}
    )
    assert new_product.name == "Orange"
    assert new_product.description == "Krasnodar Orange"
    assert new_product.price == 50.1
    assert new_product.quantity == 10


def test_new_product_product_exists():
    new_product = Product.new_product(
        {"name": "Ananas", "description": "Krasnodar Ananas", "price": 50.1, "quantity": 10}
    )
    assert new_product.quantity == 10
    assert new_product.price == 50.1
    new_product = Product.new_product(
        {"name": "Ananas", "description": "Krasnodar Ananas", "price": 60.1, "quantity": 5}
    )
    assert new_product.quantity == 15
    assert new_product.price == 60.1


@patch("builtins.input")
def test_price(mock_input):
    new_product = Product.new_product({"name": "Lemon", "description": "Krasnodar Lemon", "price": 50, "quantity": 10})
    assert new_product.price == 50

    new_product.price = 60
    assert new_product.price == 60

    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        new_product.price = 0

    mock_input.return_value = "y"
    new_product.price = 50
    assert new_product.price == 50

    mock_input.return_value = "n"
    new_product.price = 40
    assert new_product.price == 50


def test_product_str(product):
    assert str(product) == "Apple, 50.1 руб. Остаток: 10"


def test_product_add(product, product2):
    result = product + product2
    assert result == 6511
