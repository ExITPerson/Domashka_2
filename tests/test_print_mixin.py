from pytest import CaptureFixture

from src.lawn_grass_products import LawnGrass
from src.products import Product
from src.smartphone_products import Smartphone


def test_print_mixin(capsys: CaptureFixture) -> None:
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    message2 = capsys.readouterr()
    assert message2.out.strip() == "LawnGrass(Газонная трава 2, Выносливая трава, 450.0, 15)"

    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    message3 = capsys.readouterr()
    assert message3.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)"
