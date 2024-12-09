from src.lawn_grass_products import LawnGrass
from src.products import Product
from src.smartphone_products import Smartphone
from abc import ABC, abstractmethod

class Abstract(ABC):

    @abstractmethod
    def print_count_products_in_stock(self):
        pass


class Order(Abstract):

    def __init__(self, product: Product, order_count: int) -> None:
        self.product = product
        self.order_count = order_count
        self.total_price = self.order_count * self.product.price
        self.product.quantity -= self.order_count

    def __repr__(self):
        return f"Товар: {self.product.name}, количество: {self.order_count}, итоговая цена: {self.total_price}"

    def print_count_products_in_stock(self):
        return self.product.quantity


class Category(Abstract):
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self) -> str:
        count = 0
        for product in self.__products:
            count += product.quantity
        return f"{self.name}, количество продуктов: {count}"

    def add_product(self, product: Product) -> None:
        if isinstance(product, (Product, LawnGrass, Smartphone)):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> str:
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity}\n"
        return product_str

    @property
    def products_in_list(self) -> list:
        return self.__products

    def print_count_products_in_stock(self):
        return Category.product_count


