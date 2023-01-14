class Products:
    def __init__(self, product_name, price, color):
        self.product_name = product_name
        self.price = price
        self.color = color

    @property
    def color_(self):
        return self.color

    @color_.setter
    def color_(self, new):
        self.color = new


product = Products("olma", 3000, "qizil")
# print(product.color_)
new = "kok"
product.color_ = new
# print(product.color_)
