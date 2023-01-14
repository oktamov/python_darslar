class Country:
    def __init__(self, name, capital, country_area, people):
        self.name = name
        self.capital = capital
        self.country_area = country_area
        self.people = people

    def get_info(self):
        country_info = f"nomi {country.name}, poytaxt {country.capital}, maydoni {country.country_area}, aholisi {country.people} "
        return country_info


country = Country

print(f'davlat  malumotini kirit: ')
country.name = input(" name: ")
country.capital = input("capital: ")
country.country_area = input("country_area: ")
country.people = int(input("aholisi "))

print(country.get_info())
