from tests.conftest import product

from src.products import Product


def test_product(product):
    assert product.name == "Apple"
    assert product.description == "Golden apple"
    assert product.price == 50.1
    assert product.quantity == 10