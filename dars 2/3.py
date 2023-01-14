class Products:
    def __init__(self, product_name, price, country, when, color):
        self.product_name = product_name
        self.price = price
        self.country = country
        self.when = when
        self.color = color


product = Products
products = ""
for i in range(1, 3):
    print(f'mahsulot {i} malumotini kirit: ')
    product.product_name = input("product name: ")
    product.price = input("price: ")
    product.country = input("country: ")
    product.when = input("when: ")
    product.color = input("color: ")
    product_info = f"nomi {product.product_name}, narxi {product.price} so'm, davlati {product.country}, yili {product.when}, rangi {product.color} "
    products+=product_info
print(products)
