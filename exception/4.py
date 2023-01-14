def count_the(file_name):
    count = 0
    with open(file_name, 'r') as f:
        for line in f:
            if 'the' in line.lower():
                count += 1
    return count


print(count_the("test.txt"))
