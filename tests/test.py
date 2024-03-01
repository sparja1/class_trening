import pytest

from src.classes import Category, Product


@pytest.fixture
def class_category():
    return Category('Телевизоры',
                    "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                    {
                        "name": "55\' QLED 4K",
                        "description": "Фоновая подсветка",
                        "price": 123000.0,
                        "quantity": 7
                    })


def test_category_init(class_category):
    assert class_category.name == 'Телевизоры'
    assert class_category.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    assert class_category.products == {
        "name": "55\' QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7}
    assert class_category.number_of_category == 1
    assert class_category.count_of_product == 1


def test_get_name(class_category):
    assert class_category.get_name() == "Телевизоры"


def test_get_description(class_category):
    assert class_category.get_description() == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"


def test_get_products(class_category):
    assert class_category.get_products() == {
        "name": "55\' QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7}


@pytest.fixture
def product_init():
    return Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)


def test_product_init(product_init):
    assert product_init.get_name() == "55\" QLED 4K"
    assert product_init.get_description() == "Фоновая подсветка"
    assert product_init.get_price() == 123000.0
    assert product_init.get_quantity() == 7


def test_get_name(product_init):
    assert product_init.get_name() == "55\" QLED 4K"


def test_get_description(product_init):
    assert product_init.get_description() == "Фоновая подсветка"


def test_get_price(product_init):
    assert product_init.get_price() == 123000.0


def test_get_quantity(product_init):
    assert product_init.get_quantity() == 7
