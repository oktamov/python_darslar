class Students:
    def __init__(self, first_name, last_name, age):
        self.ism = first_name
        self.familiya = last_name
        self.yosh = age


from18to25 = ""
talaba_info = []

student1 = Students
for i in range(1, 3):
    print(f'talaba {i} malumotini kirit: ')
    student1.first_name = input("ismi: ")
    student1.last_name = input("familiya: ")
    student1.age = int(input("yoshi: "))
    student1_info = f"ism {student1.first_name}, familiya {student1.last_name}, yosh {student1.age}"
    talaba_info.append(student1_info)
    if student1.age >= 18 and student1.age <= 25:
        from18to25 += student1_info

print(f"18 dan 25 yoshgacha {from18to25}\n")
print(f"talabalar malumoti {talaba_info}\n")
#
# print('talaba 2 malumotini kirit: ')
# student2 = Students
# student2.first_name = input("ismi: ")
# student2.last_name = input("familiya: ")
# student2.age = int(input("yoshi: "))
# student2_info = f"ism {student2.first_name}, familiya {student2.last_name}, yosh {student2.age}"
# talaba_info.append(student2_info)
# if student2.age >= 18 and student2.age <= 25:
#     from18to25.append(student2_info)
#
# print('talaba 3 malumotini kirit: ')
# student3 = Students
# student3.first_name = input("ismi: ")
# student3.last_name = input("familiya: ")
# student3.age = int(input("yoshi: "))
# student3_info = f"ism {student3.first_name}, familiya {student3.last_name}, yosh {student3.age}"
# talaba_info.append(student3_info)
# if student3.age >= 18 and student3.age <= 25:
#     from18to25.append(student3_info)

