nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Prime numbers:")
for i in range(2, len(nums)):
    primes = list(filter(lambda x: x % i != 0, nums))
    print(i, primes)
