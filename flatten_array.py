def flatten_arr(li):
    """
    Flattens list of arbritrary lists using recursion.

    >>> flatten_arr(flatten_arr([1, 2, [3, 4, [5]]]))
    [1, 2, 3, 4, 5]

    >>> flatten_arr([])
    []
    """
    flattened_arr = []

    for item in li:
        if type(item) is list:
            flattened_arr.extend(flatten_arr(item))
        else:
            flattened_arr.append(item)

    return flattened_arr

if __name__ == '__main__':
    import doctest
    doctest.testmod()
