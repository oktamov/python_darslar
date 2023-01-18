import csv


def get_population_20M():
    res = {}
    with open("../csv/countries of the world.csv") as f:
        data = [row for row in csv.reader(f)]
    for line in data[1:]:
        coutry, count = line[0].strip(), int(line[2].strip())
        if count >= 2000000:
            res[coutry] = count
    return res



def get_countries_xith_c():
    result = []
    with open("../csv/countries of the world.csv") as f:
        data = [row for row in csv.reader(f)]

    for line in data[1:]:
        name = line[0].strip()
        if name.startswith("C"):
            result.append(name)

    return result


def write_country_c():
    with open('coutry_c.txt', 'w') as file:
        for country in get_countries_xith_c():
            file.write(f'{country}\n')


def get_gdp_10000():
    res = {}
    with open("../csv/countries of the world.csv") as f:
        data = [row for row in csv.reader(f)]
    try:
        for line in data[1:]:
            coutry, count = line[0].strip(), int(line[8].strip())
            if count >= 10000:
                res[coutry] = count
    except Exception as e:
        pass


    return res



# print(write_country_c())

# print(get_population_20M())
print(get_gdp_10000())
