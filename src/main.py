from src.classes import open_file
from src.classes import Category, Product


def main():
    for cateqoryes in open_file():
        category = Category(cateqoryes['name'], cateqoryes['description'], cateqoryes['products'])
        # print(f"{category.get_name()}\n{category.get_description()}\n{category.get_products()}")

        for products in cateqoryes['products']:
            product = Product(products["name"], products['description'], products['price'], products['quantity'])
            # print(f"{product.get_name()}\n{product.get_description()}\n{product.get_price()}\n{product.get_quantity()}")


if __name__ == "__main__":
    main()
