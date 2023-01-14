class University:
    def __init__(self, univerity_name):
        self.univerity_name = univerity_name

    def get_main_info(self):
        return self.univerity_name

    @property
    def universityname_(self):
        return self.univerity_name

    @universityname_.setter
    def universityname_(self, new):
        self.univerity_name = new


class Direktor(University):
    def __init__(self, univerity_name, full_name, age):
        super().__init__(univerity_name)
        self.full_name = full_name
        self.age = age

    def get_direktor_info(self):
        return f"{self.univerity_name}ning direktori-{self.full_name}, yoshi {self.age} da"


class Xodimlar(University):
    def __init__(self, univerity_name, full_name, age, job):
        super().__init__(univerity_name)
        self.full_name = full_name
        self.age = age
        self.job = job

    def get_xodimlar_info(self):
        return f"{self.univerity_name} ning {self.job} - {self.full_name}, uning yoshi - {self.age} da"


class Teachers(University):
    def __init__(self, univerity_name, full_name, lesson):
        super().__init__(univerity_name)
        self.full_name = full_name
        self.lesson = lesson

    def get_teacher_info(self):
        return f"{self.univerity_name} ning oqituvchisi - {self.full_name}, u {self.lesson}dan dars beradi"


class Students(University):
    def __init__(self, univerity_name, full_name, kurs):
        super().__init__(univerity_name)
        self.full_name = full_name
        self.kurs = kurs

    def get_student_info(self):
        return f"{self.univerity_name} ning talabasi - {self.full_name}, u {self.kurs} - kurs talabasi"


university = University("PDP")
new = "Milliy"
university.universityname_ = new
direktor = Direktor(university.univerity_name, "AA", 40)
xodimlar = Xodimlar(university.univerity_name, "AA", 30, "qoravul")
teacher = Teachers(university.univerity_name, "AA", "python")
students = Students(university.univerity_name, "AA ", 3)





def info():
    info_ = f"Universitet:  {university.get_main_info()}\n" \
            f"Direktor:  {direktor.get_direktor_info()}\n" \
            f"Xodimlar:  {xodimlar.get_xodimlar_info()}\n" \
            f"O'qituvchi:  {teacher.get_teacher_info()}\n" \
            f"Talaba:  {students.get_student_info()}"
    return info_


print(info())
