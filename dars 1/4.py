class Cars:
    def __init__(self, name, color, year):
        self.nomi = name
        self.rangi = color
        self.yili = year


to_10 = []
for i in range(1,11):
    print(f'mashina {i} malumotini kirit: ')
    car1 = Cars
    car1.name = input("nomi: ")
    car1.color = input("rangi: ")
    car1.year = int(input("yili: "))
    car1_info = f"nomi {car1.name}, rangi {car1.color}, yili {car1.year}"
    if 2022 - car1.year >= 10:
        to_10.append(car1_info)
print(f"10 yildan oshga mashinalar {to_10}")
# print('mashina 2 malumotini kirit: ')
# car2 = Cars
# car2.name = input("nomi: ")
# car2.color = input("rangi: ")
# car2.year = int(input("yili: "))
# car2_info = f"nomi {car2.name}, rangi {car2.color}, yili {car2.year}"
# if 2022 - car2.year >= 10:
#     to_10.append(car2_info)
#
# print('mashina 3 malumotini kirit: ')
# car3 = Cars
# car3.name = input("nomi: ")
# car3.color = input("rangi: ")
# car3.year = int(input("yili: "))
# car3_info = f"nomi {car3.name}, rangi {car3.color}, yili {car3.year}"
# if 2022 - car3.year >= 10:
#     to_10.append(car3_


