def unique(x):
    l = []
    for i in x:
        if i not in l:
            l.append(i)
    return l


list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
print(unique(list))
