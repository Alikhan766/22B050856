items = ['Mango', 'Orange', 'Apple', 'Lemon']
file = open('test.txt', 'w')
for item in items:
    file.write(item+"\n")
file.close()
