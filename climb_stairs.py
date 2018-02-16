def climb_stairs(n):
    # O(2^n)

    if n == 1:
        return 1
    if n == 2:
        return 2

    return climb_stairs(n-1) + climb_stairs(n-2)

print climb_stairs(10)

