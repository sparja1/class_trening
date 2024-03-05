from src.classes import open_file
from src.classes import Category, Product


def main():
    list_products = []
    product = Product
    for i in open_file():
        catalog = Category(i['name'], i['description'], i['products'])
        # print(f"{catalog.get_name()}\n{catalog.get_description()}\n{catalog.get_product()}")
        # print(catalog.vision_list_product)
        for producto in i['products']:
            list_products.append(producto)
            # print(product)
    print(product.created_product('Samsung Galaxy C23 Ultra', "black", 101_000.0, 100, list_products))


if __name__ == "__main__":
    main()
