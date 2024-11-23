class Product:
    name: str
    description: str
    price: float
    quantity: int

    products = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, product_dict: dict):
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
    def price(self):
        return self.__price


    @price.setter
    def price(self, price):
        if price <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        elif 0 < price < self.__price:
            user_input = input("Поменять цену? (y / n) ").lower()
            if user_input == "y":
                self.__price = price
        else:
            self.__price = price


