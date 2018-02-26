def is_prime(n):
    """
    Runtime: O(sqrt(n))
    """
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print is_prime(33)

def counts_ltrs(string):
    counts_dict = {}
    for char in string:
        counts_dict[char] = counts_dict.get(char, 0) + 1

    return counts_dict

print len(counts_ltrs('taco cat'))

