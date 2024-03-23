import json
from abc import ABC, abstractmethod


class Category:
    """ Класс категории """
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
        """ Функция вывода названия """
        return self.name

    def get_description(self):
        """ Функция вывода описания """
        return self.description

    def get_products(self):
        """ Функция списка товара """
        return self.__products

    def add_product(self, product):
        """ Функция добавления нового продукта """

        if isinstance(product, Product):
            if product.quantity == 0:
                raise ValueError('Нельзя добавить товар с нулевым количеством')
            else:
                self.__products.append(product)
                print('Товар добавлен')
                return self.__products
        else:
            raise TypeError("Добавлять можно только объекты Product и его наследников")


    @property
    def get_goods(self):
        """ Вернет все товары которые находятся в products """
        result = []
        for product in self.__products:
            result.append(f"{product.name}, {product.get_price} руб. Остаток: {product.quantity} шт.")
        return result

    def average_price_all_products(self):
        """Метод подсчета средней цены товаров"""
        total_price = sum([product.price for product in self.__products])
        total_quantity = len(self.__products)
        try:
            return total_price / total_quantity
        except ZeroDivisionError:
            return 0

    def __str__(self):
        """ Функция количества через магический метод str """
        product_count = 0
        self.category_name = self.name
        for i in self.__products:
            product_count += i.quantity

        return f"{self.category_name}, количество продуктов: {product_count} шт"

    def __len__(self):
        """ Функция количества через магический метод len """
        return sum([product.quantity for product in self.__products])


class MixinLog:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Объект {self.__class__.__name__} был создан со следующими атрибутами:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name, description, price, quantity, color):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.color = color

    @abstractmethod
    def __str__(self):
        return (f' Название - {self.name}\n, Описание - {self.description}\n, '
                f'Цена - {self.price}\n, Количество - {self.quantity}\n, Цвет - {self.color}\n')


class Product(MixinLog, BaseProduct):
    """ Класс продукты """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int, color: str):
        """ Функция иницилизации """
        super().__init__(name=name, description=description, price=price, quantity=quantity, color=color)
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color

    def get_name(self):
        """ Функция вывода названия товара """
        return self.name

    def get_description(self):
        """ Функция вовода описания товара """
        return self.description

    @property
    def get_price(self):
        """ Функция вывода стоимости товара """
        return self.__price

    @get_price.setter
    def get_price(self, value):
        if value <= 0:
            print("Цена введена некорректно")
        else:
            self.__price = value

    def get_quantity(self):
        """ Функция вывода количества """
        return self.quantity

    @classmethod
    def created_product(cls, name: str, description: str, price: float, quantity: int, color: str):
        """ Метод добавления нового продукта
        :return: Новый продукт, который можно добавить """
        new_product = cls(name, description, price, quantity, color)
        return new_product

    def __str__(self):
        """ Функция количества через магический метод str """
        return f'{self.name}, {self.get_price} руб. Остаток: {self.quantity}, Цвет: {self.color} '

    def __add__(self, other):
        """ Метод сложения суммы товара """
        if self.quantity == 0 or other.quantity == 0:
            raise ValueError("Нельзя добавить товар с нулевым количеством")

        if type(other) is type(self):
            total_amount = (self.__price * self.quantity) + (other.__price * other.quantity)
            return total_amount
        else:
            raise TypeError


class Smartphone(Product, MixinLog):
    """ Класс смартфоон """
    performance: int
    model: str
    memory_capacity: int
    color: str

    def __init__(self, name, description, price, quantity, color, performance, model, memory_capacity, ):
        super().__init__(name=name, description=description, price=price, quantity=quantity, color=color)
        self.performance = performance
        self.model = model
        self.memory_capacity = memory_capacity

    def __str__(self):
        return super().__str__() + f"Производительность: {self.performance} Модель: {self.model}, " \
                                 f"Объем встроенной памяти: {self.memory_capacity}gb"


class LawnGrass(Product, MixinLog):
    """ Класс Трава газонная """
    manufacturer_country: str
    germination_period: int

    def __init__(self, name, description, price, quantity, color, manufacturer_country, germination_period):
        super().__init__(name=name, description=description, price=price, quantity=quantity, color=color)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period

    def __str__(self):
        return super().__str__() + f"Cтрана-производитель: {self.manufacturer_country} " \
                                   f"Cрок прорастания: {self.germination_period} дней"


def open_file():
    """ Функция открытия файла """
    with open('products.json', 'r', encoding="utf-8") as data:
        list_operations = json.load(data)
        return list_operations

