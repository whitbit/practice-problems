def is_happy(n):

    mem = set()

    while n != 1:
        n = sum([int(i) ** 2 for i in str(n)])
        print n
        if n in mem:
            return False
        mem.add(n)
    return True