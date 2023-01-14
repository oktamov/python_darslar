class Aviakassa:
    ADDRESS = {
        "fargona": 300,
        "namangan": 350,
        "andijon": 400
    }
    SERVIS = {
        "ha": 10,
        "yoq": 0,
    }

    def __init__(self, airplane, service, people):
        self.airplane = airplane
        self.servise = service
        self.people = people

    def get_info(self):
        info = f"\nSizning broningiz: Joylashuv - {aviakassa.airplane}, \nQoshimcha xizmatlaar - {aviakassa.servise}," \
               f" \nOdam - {aviakassa.people} kishi \nUmumiy narxi - {self.price_change()} $"
        return info

    def price_change(self):
        price = 0
        if aviakassa.airplane in self.ADDRESS:
            price += self.ADDRESS.get(aviakassa.airplane)

        if aviakassa.servise in self.SERVIS:
            price += self.SERVIS.get(aviakassa.servise)

        return price * aviakassa.people


address = input("Qayerdan borasz:\nfargona - 300$\nnamangan - 350$\nandijon - 400$\n>>> ")
service = input("Qoshimcha xizmatlar mavjudmi:\nha - 10$\nyoq - tekin\n>>> ")
people = int(input("Necha kishi borasz: "))

aviakassa = Aviakassa(address, service, people)

print(aviakassa.get_info())
