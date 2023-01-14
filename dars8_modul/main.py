from java import Java
from python import Python
from javascript import Javascript


def exam():
    if java.get_grade() >= 60 and python.get_grade() >= 60 and javascript.get_grade() >= 60:
        return "imtihondan otdi"
    else:
        return 'otolmadi'


java = Java(60)
python = Python(90)
javascript = Javascript(60)
print(exam())
