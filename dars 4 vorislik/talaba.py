class Person:
    def get_main_info(self):
        info = f"Otasi:  ism familiyasi - {self.name_upper(father.fullname)}, yoshi - {father.age} da\n" \
               f"Onasi:  ism familiyasi - {self.name_upper(mother.fullname)}, yoshi - {mother.age} da\n" \
               f"Talaba:  ism familiyasi - {self.name_upper(talaba.fullname)}, yoshi - {talaba.age} da, {talaba.kurs} - kurs talabasi\n"
        return info

    @staticmethod
    def name_upper(name):
        return name.title()


class Father(Person):
    def __init__(self, fullname, age):
        self.fullname = fullname
        self.age = age


class Mother(Person):
    def __init__(self, fullname, age):
        self.fullname = fullname
        self.age = age


class Talaba(Father, Mother):
    def __init__(self, fullname, age, kurs):
        super().__init__(fullname, age)
        super().__init__(fullname, age)
        self.kurs = kurs

    @property
    def kurs_(self):
        return talaba.kurs

    @kurs_.setter
    def kurs_(self, new_kurs):
        talaba.kurs = new_kurs


person = Person()

father = Father(" ali valiyev", 40)

mother = Mother("guli aliyeva", 38)

talaba = Talaba("olim olimov", 19, 3)

new_kurs = 4
talaba.kurs_ = new_kurs

print(person.get_main_info())
