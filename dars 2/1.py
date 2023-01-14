class Students:
    def __init__(self, first_name, last_name, age, lesson_grade):
        self.ism = first_name
        self.familiya = last_name
        self.yosh = age
        self.lesson_grade = lesson_grade

    def get_info(self):
        info = f"toliq ism {student1.ism} {student1.familiya} yosh {student1.yosh} fanlar royxati va bahosi {student1.lesson_grade}"
        return info

    @staticmethod
    def get_middle_grade():
        sum_ = 0
        sanoq = 0
        for key, val in student1.lesson_grade.items():
            sum_ += val
            sanoq += 1
        return sum_ / sanoq


student1 = Students("ali", "valiyev", 20, {"python": 5, "java": 4, "PHP": 3})

print(student1.get_info())
print(student1.get_middle_grade())
