import pytest

from src.classes import Category, Product, ExceptionsZeroQuantity


@pytest.fixture
def class_category():
    return Category('Телевизоры',
                    "Современный телевизор, который позволяет наслаждаться "
                    "просмотром, станет вашим другом и помощником",
                    {"name": "55\' QLED 4K", "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7})


def test_category_init(class_category):
    assert class_category.name == 'Телевизоры'
    assert class_category.description == ("Современный телевизор, который позволяет наслаждаться просмотром, "
                                          "станет вашим другом и помощником")
    assert class_category.get_products() == {
        "name": "55\' QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7}
    assert class_category.category_count == 1
    assert class_category.product_count == 4


def test_get_name(class_category):
    assert class_category.get_name() == "Телевизоры"


def test_get_description(class_category):
    assert class_category.get_description() == ("Современный телевизор, который позволяет наслаждаться просмотром,"
                                                " станет вашим другом и помощником")


def test_get_products(class_category):
    assert class_category.get_products() == {
        "name": "55\' QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7}


@pytest.fixture
def product_init():
    return Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7, 'green')


def test_product_init(product_init):
    assert product_init.get_name() == "55\" QLED 4K"
    assert product_init.get_description() == "Фоновая подсветка"
    assert product_init.get_price == 123000.0
    assert product_init.get_quantity() == 7


def test_product_name(product_init):
    assert product_init.get_name() == "55\" QLED 4K"


def test_product_description(product_init):
    assert product_init.get_description() == "Фоновая подсветка"


def test_product_price(product_init):
    assert product_init.get_price == 123000.0


def test_product_quantity(product_init):
    assert product_init.get_quantity() == 7


def test__add__metod():
    product1 = Product("Product A", "Description A", 100.0, 10, "green")
    product2 = Product("Product A", "Description A", 300.0, 5, "black")
    assert product1 + product2 == 2500.0


def test__add__metod_error():
    product1 = Product("Product A", "Description A", 100.0, 10, "green")
    category = Category("Product A", "Description A", [])
    with pytest.raises(TypeError):
        product1 + category


def test_add_product_without_zero_quantity():
    category = Category("Test Category", "Description", [])
    product_non_zero_qty = Product("Product Non Zero Qty", "Description", 20.0, 5, "green")

    try:
        category.add_product(product_non_zero_qty)
    except ExceptionsZeroQuantity:
        pytest.fail("")


