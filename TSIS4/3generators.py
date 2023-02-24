def generator(n):
    for i in range(0, n):
        if i % 3 == 0 and i % 4 == 0:
            yield i


for j in generator(50):
    print(j)
