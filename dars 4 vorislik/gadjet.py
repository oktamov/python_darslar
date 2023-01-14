class Gadjet:
    def get_info(self):
        return f"telefon:  nomi - {telefon.name}, rangi - {telefon.color}, xotirasi - {telefon.storage}\n" \
               f"Kompyuter:  nomi - {computer.name}, rangi - {computer.color}, xotirasi - {computer.storage}\n" \
               f"Televizor:  nomi - {televizor.name}, rangi {televizor.color}"

    @property
    def color_(self):
        return self.color

    @color_.setter
    def color_(self, new):
        self.color = new


class Telefon(Gadjet):
    def __init__(self, name, color, storage):
        self.name = name
        self.color = color
        self.storage = storage


class Computer(Gadjet):
    def __init__(self, name, color, storage):
        self.name = name
        self.color = color
        self.storage = storage


class Televizor(Gadjet):
    def __init__(self, name, color):
        self.name = name
        self.color = color


gadjet = Gadjet()

telefon = Telefon("A51", "oq", 128)
new = "qora"
telefon.color_ = new

computer = Computer("MSI", "black", "1 tb HDD + 256 gb SSD")
computer.color_ = new

televizor = Televizor("samsung", "qora")

print(gadjet.get_info())
