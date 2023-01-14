def read_file(file_name):
    count = 0
    with open(file_name, 'r') as f:
        for line in f:
            for i in range(len(line)):
                if line[i] == ' ':
                    count += 1
            count += 1
    return count


print(read_file("test.txt"))
