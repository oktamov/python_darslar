a = "3,4,5"
sum_ = 0
for i in a.split(","):
    i = int(i)
    sum_ += i
    print(type(i))
print(sum_ // 3)
