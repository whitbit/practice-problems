
def max_profits(stock_prices):
    """
    Return max profit using brute force method. O(n^2) solution.

    >>> max_profits([10, 7, 5, 11, 9])
    6

    >>> max_profits([1, 2, 3, 5])
    4

    >>> max_profits([])
    0
    """

    max_profits = 0

    for i in range(len(stock_prices)):
        for j in range(i + 1, len(stock_prices)):
            price_difference = stock_prices[j] - stock_prices[i]
            if price_difference > 0:
                if price_difference > max_profits:
                    max_profits = price_difference

    return max_profits


def get_max_profit(stock_prices):
    """
    Return max profits using the greedy approach (O(n)).
    Simply update the best answer so far.
    
    >>> get_max_profit([10, 7, 5, 11, 9])
    6

    >>> get_max_profit([1, 2, 3, 5])
    4

    >>> get_max_profit([3, 3, 3, 3])
    0

    >>> get_max_profit([4, 3, 2, 1])
    -1

    """
    if len(stock_prices) < 2:
        raise IndexError('Getting a profit requires more than 2 stock prices.')

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for i, current_price in enumerate(stock_prices):

        if i == 0:
            continue

        profit = current_price - min_price

        max_profit = max(max_profit, profit)

        min_price = min(current_price, min_price)

    return max_profit


if __name__ == '__main__':
    import doctest
    doctest.testmod()