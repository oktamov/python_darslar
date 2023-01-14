class PetHouse:
    PRICE_TYPES = {
        "it": 20,
        "mushuk": 10
    }
    SERVIS = {
        "ha": 5,
        "yoq": 0
    }

    def __init__(self, type_pet, service, stay_time):
        self.type_pet = type_pet
        self.servise = service
        self.stay_time = stay_time

    def get_info(self):
        info = f"\nUy hayvoningiz broni : \nhayvon turi - {house.type_pet}, \nQoshimcha xizmatlaar - {house.servise}," \
               f" \nMuddat - {house.stay_time} kun \numumiy narxi - {self.price_change()} $"
        return info

    def price_change(self):
        price = 0
        if house.type_pet in self.PRICE_TYPES:
            price += self.PRICE_TYPES.get(house.type_pet)

        if house.servise in self.SERVIS:
            price += self.SERVIS.get(house.servise)

        return house.stay_time * price


type_pet = input("Uy hayvoningiz turi:\nit\nmushuk\n>>> ")
service = input("Qoshimcha xizmatlar mavjudmi:\nha/yoq\n>>> ")
stay_time = int(input("Qancha muddat qoladi: "))

house = Pet_House(type_pet, service, stay_time)

print(house.get_info())
