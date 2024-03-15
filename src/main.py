from src.classes import open_file
from src.classes import Category, Product, Smartphone, LawnGrass


def main():
    for cat in open_file():
        category = Category(cat['name'], cat["description"], [])
        # print(category.get_goods)
        for product_data in cat['products']:
            product = Product(product_data['name'], product_data["description"],
                              product_data['price'], product_data['quantity'], '')
            category.add_product(product)

        new_product = Product.created_product('nokia', 'dark', 10_000.0, 10, "черный")
        category.add_product(new_product)
        print(category.get_goods)
        print(category)
        print(len(category))
        print(new_product)

    product1 = Product("patiphon", "есть", 100.0, 10, 'red')
    product2 = Product("simens", "нет", 200.0, 5, 'blue')

    # Выполним сложение двух продуктов
    total_price = product1 + product2
    print(f"Суммарная стоимость продуктов: {total_price}")

    product1 = Smartphone('samsung', 'aaaa', 100000.0, 100, 'black', 10000, 'galaxy', 10)
    product2 = LawnGrass('ТРАВА', 'aaa', 100.0, 1000000, 'green', 'Russia', 20)
    print(product1)
    print(product2)



if __name__ == "__main__":
    main()