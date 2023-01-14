class Students:
    yosh = 10

    def __init__(self, first_name, last_name, birthday, lesson_grade):
        self.ism = first_name
        self.familiya = last_name
        self.birthday = birthday
        self.lesson_grade = lesson_grade

    def get_info(self):
        info = f"toliq ism {student1.ism} {student1.familiya} yosh {student1.birthday} fanlar royxati va bahosi {student1.lesson_grade}"
        return info

    @classmethod
    def get_age(cls, age):
        student1.birthday = age


student1 = Students("ali", "valiyev", 2002, {"python": 5, "java": 4, "PHP": 3})

student1.get_age(2022 - student1.birthday)

print(student1.get_info())
