import csv


def total_case_100000_1000000():
    res = ""
    with open("../csv/worldometer_data.csv", encoding="utf-8") as f:
        data = [row for row in csv.reader(f)]
    for line in data[1:]:
        total_case = int(line[3].strip())
        if 1000000 >= total_case >= 100000:
            res += f"{line}\n"
    return res


def write_total_cases():
    with open("total case.csv", "w", encoding="utf-8") as f:
        for line in total_case_100000_1000000():
            f.write(line)


def get_countryin_activecase():
    res = ""
    a = input("kirit: ")
    with open("../csv/worldometer_data.csv", encoding="utf-8") as f:
        data = [row for row in csv.reader(f)]
    for line in data[1:]:
        if a == line[0].strip():
            res += f"{line[9].strip()}"
    return res

def get_continent_totalcase():
    res = ""
    a = input("kirit: ")
    with open("../csv/worldometer_data.csv", encoding="utf-8") as f:
        data = [row for row in csv.reader(f)]
    for line in data[1:]:
        if a == line[1].strip():
            res += f"{line[3].strip()}\n"
    return res

print(get_continent_totalcase())
# print(get_countryin_activecase())

# write_total_cases()
# print(total_case_100000_1000000())
