from products import Product
from category import Category


class ProductIterator:

    def __init__(self, category_obj):
        self.category = category_obj
        self.sum = 0
        self.index = 0


    def __iter__(self):
        return self


    def __next__(self):
        for product in self.category.products_in_list:
            if self.index < len(self.category.products_in_list):
                self.sum += product.price * product.quantity
                self.index += 1
            else:
                raise StopIteration
        return self.sum


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3])

    iterator = ProductIterator(category1)

    for i in iterator:
        print(i)