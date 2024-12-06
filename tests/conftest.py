import pytest

from src.category import Category
from src.lawn_grass_products import LawnGrass
from src.product_iterator import ProductIterator
from src.products import Product
from src.smartphone_products import Smartphone


@pytest.fixture
def product() -> Product:
    return Product("Apple", "Golden apple", 50.1, 10)


@pytest.fixture
def product2() -> Product:
    return Product("Grape", "Krasnodar grape", 60.1, 100)


@pytest.fixture
def product_iterator(category: Category) -> ProductIterator:
    return ProductIterator(category)


@pytest.fixture
def category_farm() -> Category:
    return Category("Farm fruits", "Farm fruits", ["Apple", "Pear", "Cherry"])


@pytest.fixture
def category_citrus() -> Category:
    return Category("Citrus fruits", "Citrus fruits", ["Orange", "Grape", "Limon", "Broomstick"])


@pytest.fixture
def category(product: Product, product2: Product) -> Category:
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product, product2],
    )
    return category1


@pytest.fixture
def smartphone1() -> Smartphone:
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    return smartphone


@pytest.fixture
def smartphone2() -> Smartphone:
    smartphone = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    return smartphone


@pytest.fixture
def lawn_grass1() -> LawnGrass:
    lawn_grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    return lawn_grass


@pytest.fixture
def lawn_grass2() -> LawnGrass:
    lawn_grass = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    return lawn_grass


@pytest.fixture
def category_crass(lawn_grass1: LawnGrass, lawn_grass2: LawnGrass) -> Category:
    return Category("Газонная трава", "Различные виды газонной травы", [lawn_grass1, lawn_grass2])


@pytest.fixture
def category_smartphone(smartphone1: Smartphone, smartphone2: Smartphone) -> Category:
    return Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
