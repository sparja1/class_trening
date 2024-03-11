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
        #print(category.get_goods)
        print(category)
        print(len(category))
        print(new_product)

    product1 = Product("patiphon", "есть", 100.0, 10)
    product2 = Product("simens", "нет", 200.0, 5)

    # Выполним сложение двух продуктов
    total_price = product1 + product2
    print(f"Суммарная стоимость продуктов: {total_price}")


if __name__ == "__main__":
    main()