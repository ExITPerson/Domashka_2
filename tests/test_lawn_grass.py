import pytest


def test_smartphone(lawn_grass1):
    assert lawn_grass1.name == "Газонная трава"
    assert lawn_grass1.country == "Россия"


def test_add_smartphone(smartphone1, lawn_grass2, lawn_grass1):
    sum1 = lawn_grass2 + lawn_grass1

    assert sum1 == 16750

    with pytest.raises(TypeError):
        smartphone1 + lawn_grass1