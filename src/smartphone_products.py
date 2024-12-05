from src.products import Product

class Smartphone(Product):
    def __init__(self, name: str, description: str,
                 price: float, quantity: int, efficiency: str, model: str, memory: float, color: str,):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError

