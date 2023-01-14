class Bike_credits:
    Data_PRICE = {
        1: 5,
        2: 20,
        3: 60
    }

    def __init__(self, time, bike):
        self.time = time
        self.bike = bike

    def get_info(self):
        return f"\n{bike_credit.time} {data.get(time_)}, {bike_credit.bike} ta velosiped, \nUmumiy narx: {self.discount_price()} $"

    def data_price(self):
        price = 1
        if time_ in bike_credit.Data_PRICE:
            price = price * bike_credit.Data_PRICE.get(time_) * bike_credit.time * bike_credit.bike
        return price

    @staticmethod
    def discount_price():
        if bike_credit.bike >= 3:
            return f'Chegirma bilan: {bike_credit.data_price() - bike_credit.data_price() * 0.3}'
        else:
            return bike_credit.data_price()


data = {
    1: "soat",
    2: "kun",
    3: "hafta"
}

time_ = int(input(f"qaysi vaqt tanlaysiz: {data}\n>>>"))
if time_ in data:
    time = int(input(f"Qancha {data.get(time_)} hohlaysiz:\n>>>"))
bike = int(input("nechta velosiped olasz:\n>>>"))

bike_credit = Bike_credits(time, bike)

print(bike_credit.get_info())
