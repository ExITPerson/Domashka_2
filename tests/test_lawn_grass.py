import pytest

from src.lawn_grass_products import LawnGrass


def test_smartphone(lawn_grass1: LawnGrass) -> None:
    assert lawn_grass1.name == "Газонная трава"
    assert lawn_grass1.country == "Россия"


def test_add_smartphone(smartphone1: LawnGrass, lawn_grass2: LawnGrass, lawn_grass1: LawnGrass) -> None:
    sum1 = lawn_grass2 + lawn_grass1

    assert sum1 == 16750

    with pytest.raises(TypeError):
        smartphone1 + lawn_grass1
