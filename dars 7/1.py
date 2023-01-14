class House:
    PRICE_TYPES = {
        "oddiy": 200,
        "luks": 1000
    }

    def __init__(self, type_room, service, stay_time):
        self.type_room = type_room
        self.servise = service
        self.stay_time = stay_time

    def get_info(self):
        info = f"\nSizning broningiz: \nXona turi - {house.type_room}, \nQoshimcha xizmatlaar - {house.servise}," \
               f" \nMuddat - {house.stay_time} kun \numumiy narxi - {self.price_change()} $"
        return info

    def price_change(self):
        price = 0
        if house.type_room in self.PRICE_TYPES:
            price += self.PRICE_TYPES.get(house.type_room)
       
        return house.stay_time * price


type_room = input("qanaqa xona tanlaysiz:\noddiy\nluks\n>>> ")
service = input("qoshimcha xizmatlar mavjudmi:\nha/yoq\n>>> ")
stay_time = int(input("qancha muddat qolasz: "))

house = House(type_room, service, stay_time)

print(house.get_info())
