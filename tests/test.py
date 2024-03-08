import pytest

from src.classes import Category, Product


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
    return Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)


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


@pytest.fixture
def sample_products():
    return [
        {"name": "Product A", "description": "Description A", "price": 100.0, "quantity": 10},
        {"name": "Product B", "description": "Description B", "price": 50.0, "quantity": 20}
    ]


# def test_created_product_existing_product(sample_products):
#     result = Product.created_product("Simens", "ol", 120.0, 5, sample_products)
#     assert len(result) == 3
#     assert result[0]["quantity"] == 10
#     assert result[0]["price"] == 100.0


# def test_created_product_invalid_price(sample_products):
#     result = Product.created_product("Product", "Description", -10.0, 5, sample_products)
#     assert len(result) == 3
