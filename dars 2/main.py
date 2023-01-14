class Student:
    school_name = "PDP academy"

    def __init__(self, first_name, last_name, age, region, phone, job):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.region = region
        self.phone = phone
        self.job = job

    def get_student_info(self, middle=None):
        info = f"Full name {self.to_upper(self.get_first_name(middle))} {self.last_name}, age: {self.age_plus_5(self.age)}," \
               f" region: {self.region}, phone: {self.phone}, job: {self.job}"
        return info

    @staticmethod
    def to_upper(name):
        return name.upper()

    @staticmethod
    def age_plus_5(age):
        return age + 5

    @classmethod
    def change_school(cls, name):
        Student.school_name = name

    def get_first_name(self, middle=None):
        middle = middle if middle else ""
        return f"{self.first_name} {middle}"


student1 = Student("a", "B", 20, "Tashkent", "+999999999", "python dev")
student2 = Student("a", "B", 20, "Tashkent", "+999999999", "python dev")

# print(student1.change_school())
# print(student2.change_school())
print(student1.get_student_info())