import csv


def get_uzb_sity():
    res = ""
    with open("../csv/worldcities.csv", encoding="utf-8") as f:
        data = [row for row in csv.reader(f)]
    for line in data[1:]:
        country, sity = line[4].strip(), line[0].strip()
        if country == "Uzbekistan":
            res += f"{country} - {sity}\n"
    return res


def get_uzb_sity_location():
    res = []
    with open("../csv/worldcities.csv", encoding="utf-8") as f:
        data = [row for row in csv.reader(f)]
    for line in data[1:]:
        country = line[4].strip()
        lat = line[2].strip()
        Ing = line[3].strip()
        if country == "Uzbekistan":
            res.append(f"location=https://my-location.org/?lat={lat}&lng={Ing}")
    return res


def write_uzb_sity_location():
    with open('coutry_c.txt', 'w') as file:
        for country in get_uzb_sity_location():
            file.write(f'{country}\n')



print(write_uzb_sity_location())
print(get_uzb_sity())
# print(get_gdp_10000())
