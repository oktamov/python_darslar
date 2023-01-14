class Student1:
    def __init__(self, first_name, last_name, tel_num):
        self.ism = first_name
        self.familiya = last_name
        self.tel_raqam = tel_num


talaba1 = Student1("Ali", "Valiyev", 1234567)
talaba1_info = f"ism {talaba1.ism}, familiya {talaba1.familiya}, telefon raqami {talaba1.tel_raqam}"
talaba2 = Student1("vali", "aliyev", 1234567)
talaba2_info = f"ism {talaba2.ism}, familiya {talaba2.familiya}, telefon raqami {talaba2.tel_raqam}"
print(talaba1_info)
print(talaba2_info)


class Student2:
    def __init__(self, lesson, lesson_grade, grade_average, kirdi, chiqdi):
        self.dars = lesson
        self.dars_baho = lesson_grade
        self.ort_baho = grade_average
        self.kirgan = kirdi
        self.bitirgan = chiqdi


talaba1 = Student2("python, java, c++", "5, 4, 3", 4, 2020, None)
talaba2 = Student2("python, java, c++", "2, 4, 3", 3, 2018, 2022)
talaba1_info = f"talaba 1 ning fanlari {talaba1.dars}, baholari {talaba1.dars_baho}, otacha bahosi {talaba1.ort_baho}, oqishga kirgan yili {talaba1.kirgan}, bitirgan yili {talaba1.bitirgan}"
talaba2_info = f"talaba 1 ning fanlari {talaba2.dars}, baholari {talaba2.dars_baho}, otacha bahosi {talaba2.ort_baho}, oqishga kirgan yili {talaba2.kirgan}, bitirgan yili {talaba2.bitirgan}"
print(talaba1_info)
print(talaba2_info)
