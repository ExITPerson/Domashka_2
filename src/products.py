from typing import Any

from src.base_products import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int

    products: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity}"

    def __add__(self, other: Any) -> Any:
        if type(other) is Product:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, product_dict: dict) -> Any:
        name = product_dict["name"]
        description = product_dict["description"]
        price = product_dict["price"]
        quantity = product_dict["quantity"]

        for product in cls.products:
            if product.name == name:
                product.__price = price
                product.quantity += quantity
                return product

        new_product = cls(name, description, price, quantity)
        cls.products.append(new_product)
        return new_product

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        if price <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        elif 0 < price < self.__price:
            user_input = input("Поменять цену? (y / n) ").lower()
            if user_input == "y":
                self.__price = price
        else:
            self.__price = price
