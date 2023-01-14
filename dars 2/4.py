class Products:
    def __init__(self, product_name, price, country, when, color):
        self.product_name = product_name
        self.price = price
        self.country = country
        self.when = when
        self.color = color

    def get_info(self):
        return f"nomi {product.product_name}, narxi {self.price_format(product.price)} so'm, davlati {product.country}, yili {product.when}, rangi {product.color} "

    @staticmethod
    def price_format(price):
        return format(price,",").replace(",", " ")


product = Products("AA",10000200000,"s", 1,"d")

print(product.get_info())