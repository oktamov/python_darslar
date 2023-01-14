def count_a_m(file_name):
    counta = 0
    countm = 0
    with open(file_name, 'r') as f:
        for line in f:
            print(line)
            if 'a' in line.lower():
                counta += 1
            if 'm' in line.lower():
                countm += 1

    return f'a - {counta}, b - {countm}'


print(count_a_m("test.txt"))
