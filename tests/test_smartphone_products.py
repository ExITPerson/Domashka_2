import pytest

from src.smartphone_products import Smartphone


def test_smartphone(smartphone1: Smartphone) -> None:
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.model == "S23 Ultra"


def test_add_smartphone(smartphone1: Smartphone, smartphone2: Smartphone, lawn_grass1: Smartphone) -> None:
    sum1 = smartphone2 + smartphone1

    assert sum1 == 2580000

    with pytest.raises(TypeError):
        smartphone1 + lawn_grass1
