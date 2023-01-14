class Car:
    def __init__(self, name, color, year, speed):
        self.name = name
        self.color = color
        self.year = year
        self.speed = speed

    def get_info(self) -> str:
        return f'This car speed is {self.speed}'


class Tesla(Car):
    def __init__(self, name, color, year, speed, price):
        super().__init__(name, color, year, speed)

        self.price = price

    def get_info(self):
        result = super().get_info().replace('This', 'Tesla')
        result = result.replace(str(self.speed), str(self.speed + 30))
        return result


tesla = Tesla('Tesla', 'white', 2014, 220, 34343)
print(tesla.get_info())