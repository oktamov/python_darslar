from abc import ABC, abstractmethod, abstractproperty


class Myclass(ABC):
    def __init__(self, name):
        self.name = name

    @abstractproperty
    def name_(self):
        return self.name

    @abstractmethod
    def func(self):
        return "instance abstrac method"


class ChildClass(Myclass):
    def func(self):
        return super().func()
    @property
    def name_(self):
        return self.name


obj = ChildClass("ABC")
print(obj.func())
print(obj.name_())
