from src.products import Product

class LawnGrass(Product):
    def __init__(self, name: str, country: str, germination_period: float, color: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color