def read_file(file_name):
    count = 0
    try:
        with open(file_name, 'r') as f:
            for line in f:
                if line[0] != 'T':
                    count += 1
        return count
    except Exception:
        return "file topilmadi"


print(read_file("test.txt"))
