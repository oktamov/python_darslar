def count_this_these(file_name):
    count = 0
    with open(file_name, 'r') as f:
        for line in f:
            if 'this' in line.lower():
                count += 1
            if 'these' in line.lower():
                count += 1
    return count


print(count_this_these("test.txt"))
