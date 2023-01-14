class Texnika:
    def get_info(self):
        return f"Mashina:  nomi - {mashina.name}, rangi - {mashina.color}, yili - {mashina.yili}\n" \
               f"Avtobus:  nomi - {avtobus.name}, rangi - {avtobus.color}\n" \
               f"Tranvay:  nomi - {tranvay.name}, rangi {tranvay.color}\n" \
               f"Metro:  nomi - {metro.name}, rangi - {metro.color}"

    @property
    def color_(self):
        return self.color

    @color_.setter
    def color_(self, new):
        self.color = new


class Mashina(Texnika):
    def __init__(self, name, color, yili):
        self.name = name
        self.color = color
        self.yili = yili


class Avtobus(Texnika):
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Tranvay(Texnika):
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Metro(Texnika):
    def __init__(self, name, color):
        self.name = name
        self.color = color


gadjet = Texnika()

mashina = Mashina("Gentra", "oq", 2014)
new = "qora"
mashina.color_ = new

avtobus = Avtobus("82", "black")
avtobus.color_ = new

tranvay = Tranvay("AAA", "qora")

metro = Metro("yunusobod", "kok")

print(gadjet.get_info())
