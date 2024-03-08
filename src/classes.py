import json


class Category:
    """
    Класс категории
    """
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

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
        return self.__products

    def add_product(self, product):
        """
        Функция добавления нового продукта
        :param product:
        :return:
        """
        return self.__products.append(product)

    @property
    def get_goods(self):
        """
        Вернет все товары которые находятся в products
        :return:
        """
        result = ''
        for products in self.__products:
            result += f"{products['name']}, {products['price']}. Остаток: {products['quantity']} шт.\n"
        return result


class Product:
    """
    Класс продукты
    """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Функция иницилизации
        :param name:
        :param description:
        :param price:
        :param quantity:
        """
        self.name = name
        self.description = description
        self.__price = price
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

    @property
    def get_price(self):
        """
        Функция вывода стоимости товара
        :return:
        """
        return self.__price

    @get_price.setter
    def get_price(self, value):
        if value <= 0:
            print("Цена введена некорректно")
        else:
            self.__price = value

    def get_quantity(self):
        """
        Функция вывода количества
        :return:
        """
        return self.quantity

    @classmethod
    def created_product(cls, name, description, price, quantity):
        """
        Метод добавления нового продукта
        :param name:
        :param description:
        :param price:
        :param quantity:
        :return: Новый продукт, который можно добавить
        """
        new_product = {"name": name, "description": description, "price": price, "quantity": quantity}
        return new_product


def open_file():
    """
    Функция открытия файла
    :return:
    """
    with open('products.json', 'r', encoding="utf-8") as data:
        list_operations = json.load(data)
        return list_operations


