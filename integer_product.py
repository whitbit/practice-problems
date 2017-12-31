def get_products_of_all_ints_except_at_index(integers):
    """

    Brute force method - O(n^2) with nested loops here.

    >>> get_products_of_all_ints_except_at_index([1, 7, 3, 4])
    [84, 12, 28, 21]

    >>> get_products_of_all_ints_except_at_index([1, 0, 3, 4])
    [0, 12, 0, 0]

    >>> get_products_of_all_ints_except_at_index([]) is None
    True

    >>> get_products_of_all_ints_except_at_index([3]) is None
    True
    """

    if len(integers) < 2:
        return None

    products = []

    for i in range(len(integers)):
        product = 1
        for j in range(len(integers)):
            if i == j:
                continue
            product *= integers[j]
        products.append(product)

    return products


def get_products_except_index(integers):
    """
    Uses greedy method to obtain O(n) solution.

    >>> get_products_except_index([1, 2, 6, 5, 9])
    [540, 270, 90, 108, 60]
    """

    if len(integers) < 2:
        return None

    products = []
    product = 1

    for i in range(len(integers)):
        products.append(product)
        product *= integers[i]

    products_after = 1

    for i in range(len(integers)-1, -1, -1):
        products[i] = products[i] * products_after
        products_after *= integers[i]

    return products
  


if __name__ == '__main__':
    import doctest
    doctest.testmod()