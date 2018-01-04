# build a 2d array

# A: two substrings not the same length

def lcs(a, b):

    grid = []

    max_value = 0
    max_value_index = 0

    for i in range(len(a)):
        row = [0] * len(b)
        grid.append(row)

    for x in range(len(a)):
        for y in range(len(b)):
            if a[x] == b[y]:
                check = grid[x-1][y-1]
                grid[x][y] = check + 1

                if grid[x][y] > max_value:
                    max_value = grid[x][y]
                    max_value_index = x

    return a[(max_value_index - max_value + 1):max_value_index + 1]


print lcs('acjjjjhelloabfc', 'helloxyzlll')

# for line in grid:
#     print line


