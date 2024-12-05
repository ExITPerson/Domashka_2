from src.products import Product

class Smartphone(Product):
    def __init__(self, name: str, efficiency: str, model: str, memory: float, color: str, description: str,
                 price: float, quantity: int):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

