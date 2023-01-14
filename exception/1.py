def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            for line in f:
                return line
    except FileNotFoundError:
        return "fayl topilmadi"


read_file("testhgf.txt")
