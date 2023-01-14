def hash_display(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
        #print(content)

        return content.replace('j', 'i')


print(hash_display("test.txt"))
