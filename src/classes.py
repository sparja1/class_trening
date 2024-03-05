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
    def created_product(cls, name, description, price, quantity, list_product):
        new_product = {"name": name, "description": description, "price": price, "quantity": quantity}

        for product_add in list_product:
            if product_add['name'] == new_product['name']:
                product_add['quantity'] += new_product['quantity']
                product_add['price'] = max(product_add['price'], new_product['price'])
                return list_product

        list_product.append(new_product)
        return list_product


def open_file():
    """
    Функция открытия файла
    :return:
    """
    with open('products.json', 'r', encoding="utf-8") as data:
        list_operations = json.load(data)
        return list_operations

