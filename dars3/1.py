class Phone_13PRO:

    def __init__(self, full_name, phone, address, color, storage, price, how_many):
        self.rangi = color
        self.xotirasi = storage
        self.price = price
        self.yana = how_many
        self.full_name = full_name
        self.phone = phone
        self.address = address

    def get_info(self):
        info = f"\nsizning xaridingiz: \nnomi - Iphone 13 pro, \nrangi - {product.rangi}, \nxotirasi - {product.xotirasi}," \
               f" \nsoni - {product.yana}\numumiy narxi - {self.price_format(product.price_change())} $"
        return info

    def get_people_info(self):
        info = f"ism familiya {product.full_name}\ntelefon raqam {product.phone}\nmanzil {product.address}\n" \
               f"Tez orada mahsulotingiz yetkazib beriladi! "
        return info

    def price_change(self):
        if product.xotirasi == 128:
            product.price = 1000 * product.yana
        elif product.xotirasi == 256:
            product.price = 1050 * product.yana
        elif product.xotirasi == 512:
            product.price = 1100 * product.yana
        else:
            print("notogri yozdiz")
        return product.price

    @staticmethod
    def price_format(price):
        return format(price, ",").replace(",", " ")

    @property
    def color_(self):
        return product.rangi

    @color_.setter
    def color_(self, new):
        product.rangi = new


full_name = input("Ism familiyangizni kiriring: ")
phone = input("Telefon raqamingizni kiriring: ")
address = input("Manzilingizni kiriring: ")
color = input("Telefonni qaysi rangini tanlaysiz: qora, oq va gold >")
storage = int(input("xotirasi qanaqa bolsin: 128, 256, 512> "))
how_many = int(input("nechta buyurasiz: "))
price = 0
product = Phone_13PRO(full_name, phone, address, color, storage, price, how_many)

if color != "qora":
    new = f"uzur bizda {color} rangli qolmadi,  faqat qora ranglilar qoldi"
else:
    new = "qora"
product.color_ = new
print(product.get_info())
print(product.get_people_info())
