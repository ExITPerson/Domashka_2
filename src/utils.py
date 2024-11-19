import json
import os

from src.products import Product
from src.category import Category

def read_json(path):
    file_path = os.path.abspath(path)
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def creating_object(data):
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories
