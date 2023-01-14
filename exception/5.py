def display_words(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                if len(word) < 5:
                    print(word)




display_words("test.txt")
