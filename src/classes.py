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
        if isinstance(product, Product):
            self.__products.append(product)
        return self.__products

    @property
    def get_goods(self):
        """
        Вернет все товары которые находятся в products
        :return:
        """
        result = []
        for product in self.__products:
            result.append(f"{product.name}, {product.get_price} руб. Остаток: {product.quantity} шт.")
        return result

    def __str__(self):
        """
        Функция количества через магический метод str
        """
        product_count = 0
        self.category_name = self.name
        for i in self.__products:
            product_count += i.quantity

        return f"{self.category_name}, количество продуктов: {product_count} шт"

    def __len__(self):
        """
        Функция количества через магический метод len
        """
        return sum([product.quantity for product in self.__products])


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
    def created_product(cls, name: str, description: str, price: float, quantity: int):
        """
        Метод добавления нового продукта
        :return: Новый продукт, который можно добавить
        """
        new_product = cls(name, description, price, quantity)
        return new_product

    def __str__(self):
        """
        Функция количества через магический метод str
        """
        return f'{self.name}, {self.get_price} руб. Остаток: {self.quantity}'

    def __add__(self, other):
        """
        Метод сложения суммы товара
        """
        total_amount = (self.__price * self.quantity) + (other.__price * other.quantity)
        return total_amount


def open_file():
    """
    Функция открытия файла
    :return:
    """
    with open('products.json', 'r', encoding="utf-8") as data:
        list_operations = json.load(data)
        return list_operations
