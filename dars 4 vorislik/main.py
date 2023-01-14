class Person:
    def __init__(self, full_name, age, job, jins):
        self.full_name = full_name
        self.age = age
        self.job = job
        self.jins = jins

    def get_main_info(self):
        return f"{self.info_male_female_1()} full name is {person.full_name}, {self.info_male_female_2()} is {person.age}," \
               f" {self.info_male_female_2()} is {person.job}"

    def info_male_female_1(self):
        jinsi = ""
        if self.jins == "erkak":
            jinsi += "his"
        elif self.jins == "ayol":
            jinsi += "her"
        else:
            pass
        return jinsi

    def info_male_female_2(self):
        jinsi = ""
        if self.jins == "erkak":
            jinsi += "he"
        elif self.jins == "ayol":
            jinsi += "she"
        else:
            pass
        return jinsi


class Teacher(Person):
    def __init__(self, full_name, age, job,jins, salary):
        super().__init__(full_name, age, job, jins)
        self.salary = salary

    def get_teacher_info(self):
        return f"{self.get_main_info()}, {self.info_male_female_1()} salary is {teacher_obj.salary} $"


class Student(Person):
    def __init__(self, full_name, age, job, jins, university, kurs):
        super().__init__(full_name, age, job,jins)
        self.university = university
        self.kurs = kurs

    def get_student_info(self):
        return f"{self.get_main_info()} student, {self.info_male_female_2()} study in {student_obj.university}, {self.info_male_female_2()} is {student_obj.kurs} kurs"




  
person = Person("AA", 20, "python", "ayol")
teacher_obj = Teacher("AA", 20, "python", "erkak", 1000)
student_obj = Student("AA", 20, "talaba", "ayol", "PDP", 3)


print(person.get_main_info())
print(teacher_obj.get_teacher_info())
print(student_obj.get_student_info())
