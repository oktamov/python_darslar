import csv


def get_macbookpro_product():
    count = 0
    with open("../csv/worldcities.csv") as f:
        data = [row for row in csv.reader(f)]
    for line in data[1:]:
        product = line[1].strip()
        if product == "Macbook Pro Laptop":
            count += 1
    return count


def get_priceEach_300():
    res = []
    with open('../csv/Sales_April_2019.csv') as f:
        data = [row for row in csv.reader(f)]
    for line in data[1:]:
        price_each = int(line[3].strip())
        if price_each >= 300:
            res.append(price_each)
    return res


def write_priceEach_300():
    with open('priceEach_300.txt', 'w') as f:
        for price in get_priceEach_300():
            f.write(f"{price}\n")


print(write_priceEach_300())
# print(get_macbookpro_product())
# print(get_gdp_10000())
