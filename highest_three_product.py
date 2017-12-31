def get_highest_product_of_three(integers):
    """
    Gets highest product of any three integers in a list.
    Brute force method that is O(n^3).

    >>> get_highest_product_of_three([1,2,3])
    6

    >>> get_highest_product_of_three([1,2,3,5])
    30
    """

    highest_product = integers[0] * integers[1] * integers[2]

    for i in range(len(integers)):
        for j in range(i + 1, len(integers)):
            for k in range(j + 1, len(integers)):
                current_product = integers[i] * integers[j] * integers[k]
                if current_product > highest_product:
                    highest_product = current_product

    return highest_product

def get_highest_product_of_three_2(numbers):
    """
    O(n logn) solution: take product of max 3 nums.
    Only works if all nums are positive.

    >>> get_highest_product_of_three_2([1,2,3])
    6

    >>> get_highest_product_of_three_2([1,2,3,5])
    30


    """

    numbers.sort()

    return numbers[-3] * numbers[-2] * numbers[-1]

def get_highest_product_of_three_3(numbers):
    """

    >>> get_highest_product_of_three_3([1, 10, -5, 1, -100])
    5000

    >>> get_highest_product_of_three_3([10,2,3,5])
    150

    """

    if len(numbers) < 3:
        raise Exception('Not enough numbers.')

    highest = max(numbers[0], numbers[1])
    lowest = min(numbers[1], numbers[0])

    highest_product_of_two = numbers[0] * numbers[1]
    lowest_product_of_two = numbers[0] * numbers[1]

    highest_product_of_three = numbers[0] * numbers[1] * numbers[2]

    for i in range(2, len(numbers)):
        
        highest_product_of_three = max(
            highest_product_of_three,
            highest_product_of_two * numbers[i],
            lowest_product_of_two * numbers[i])

        highest_product_of_two = max(
            highest_product_of_two,
            numbers[i] * highest,
            numbers[i] * lowest)

        lowest_product_of_two = min(
            lowest_product_of_two,
            highest * numbers[i],
            lowest * numbers[i])
        
        highest = max(highest, numbers[i])

        lowest = min(lowest, numbers[i])


    return highest_product_of_three


if __name__ == '__main__':
    import doctest
    doctest.testmod()
