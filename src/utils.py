import json
import os
from typing import Any
from src.category import Category
from src.products import Product


def read_json(path: str) -> Any:
    file_path = os.path.abspath(path)
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def creating_object(data: dict) -> None:
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories
