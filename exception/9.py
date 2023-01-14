def hash_display(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
        for char in content:
            print(char + "#", end="")

hash_display("test.txt")
