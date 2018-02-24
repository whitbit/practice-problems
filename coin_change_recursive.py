
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

known_results = [0] * 64
def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """
    # Your code here!
    if len(haystack) < 1:
        return None
    
    if needle == haystack[0]:
        return 0
    
    index = recursive_index(needle, haystack[1:])
    
    
    if index is not None:
        return index + 1
    
    
def recMC(coin_value_list, change):
    min_coins = change
    if change in coin_value_list:
        known_results[change] = 1
        return 1
    print change
    elif known_results[change] > 0:
        return known_results[change]
    
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + recMC(coin_value_list, change - i)
            # print 'Coin {} -> Num Coins {}'.format(c, num_coins)
        if num_coins < min_coins:
            min_coins = num_coins
            known_results[change] = min_coins
    return min_coins

recMC([1, 5, 10, 25], 63)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
