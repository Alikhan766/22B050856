def string_test(s):
    UPPER_CASE = 0
    lower_case = 0

    for c in s:
        if c.isupper():
            UPPER_CASE += 1
        elif c.islower():
            lower_case += 1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", UPPER_CASE)
    print("No. of Lower case Characters : ", lower_case)


string_test('Hello, KBTU!')
