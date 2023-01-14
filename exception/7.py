def count_e(file_name):
    count = 0
    with open(file_name, 'r') as f:
        for line in f:
            words = line.lower().split()
            for word in words:
                if word[-1] == 'e':
                    count += 1
    return count


print(count_e("test.txt"))
