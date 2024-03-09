from src.classes import open_file
from src.classes import Category, Product


def main():
    for cat in open_file():
        category = Category(cat['name'], cat["description"], cat['products'])
        #print(category.get_goods)
        for product in cat['products']:
            Product(product['name'], product["description"], product['price'], product['quantity'])

        new_product = Product.created_product('nokia', 'dark', 10_000.0, 10)
        category.add_product(new_product)
        print(category.get_goods)


if __name__ == "__main__":
    main()
