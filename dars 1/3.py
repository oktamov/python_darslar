class Compyuter:
    name = 'msi'
    color = 'black'
    ram = 16
    storage = '1 tb'
    ssd = None


print('1-obyekt')
comyuter_object = Compyuter()
name = comyuter_object.name
color = comyuter_object.color
ram = comyuter_object.ram
storage = comyuter_object.storage
ssd = comyuter_object.ssd
result = f"nomi {name}, rangi {color}, ram xotirasi {ram}gb, xotirasi HDD {storage}, SSD yoq {ssd}"
print(result)
