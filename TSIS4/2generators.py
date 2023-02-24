def even_numbers(n):
    for i in range(0, n):
        if i % 2 != 0:
            yield i


n = int(input())
for i in even_numbers(n):
    print(i, end=" ")
