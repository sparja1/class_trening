import json


class Category:
    """
    Класс категории
    """
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(self.products)

    def get_name(self):
        """
        Функция вывода названия
        :return:
        """
        return self.name

    def get_description(self):
        """
        Функция вывода описания
        :return:
        """
        return self.description

    def get_products(self):
        """
        Функция списка товара
        :return:
        """
        return self.products


class Product:
    """
    Класс продукты
    """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """
        Функция иницилизации
        :param name:
        :param description:
        :param price:
        :param quantity:
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def get_name(self):
        """
        Функция вывода названия товара
        :return:
        """
        return self.name

    def get_description(self):
        """
        Функция вовода описания товара
        :return:
        """
        return self.description

    def get_price(self):
        """
        Функция вывода стоимости товара
        :return:
        """
        return self.price

    def get_quantity(self):
        """
        Функция вывода количества
        :return:
        """
        return self.quantity


def open_file():
    """
    Функция открытия файла
    :return:
    """
    with open('products.json', 'r', encoding="utf-8") as data:
        list_operations = json.load(data)
        return list_operations
