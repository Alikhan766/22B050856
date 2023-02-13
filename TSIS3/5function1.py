import itertools

if __name__ == '__main__':
    s = 'ABC'

    per = list(itertools.permutations(s))

    print([''.join(per) for per in per])
