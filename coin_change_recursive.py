
def get_coin_combos(amt, coins, current_idx=0):

    """
    >>> get_coin_combos(4, [1,2])
    3

    >>> get_coin_combos(-4, [1,2])
    0

    >>> get_coin_combos(12, [1,2,3])
    19

    """

    # BC1: if amt goes to 0, there's one combination
    if(amt == 0):
        return 1

    #BC2: if amt goes below 0, no combos and jump out of loop
    if(amt < 0):
        return 0

    num_combo = 0
    for i in range(current_idx, len(coins)):
        num_combo += get_coin_combos(amt - coins[i], coins, i)

    return num_combo

if __name__ == '__main__':
    import doctest
    doctest.testmod()