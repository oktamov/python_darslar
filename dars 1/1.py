class Students:
    def __init__(self, first_name, last_name, age):
        self.ism = first_name
        self.familiya = last_name
        self.yosh = age


        
print('talaba 1')
student = Students
student.first_name = 'Ali'
student.last_name = 'Valiyev'
student.age = 19
print(f"{student.first_name}")
print(f"{student.last_name}")
print(f"{student.age}")
