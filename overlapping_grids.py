def highest_overlapping_areas(coordinates):

    col_length = max([coordinate[0] for coordinate in coordinates])
    row_length = max([coordinate[1] for coordinate in coordinates])

    row = [0 for i in range(row_length)]
    grid = [row for col in range(col_length)]

    for coordinate in coordinates:
        height = coordinate[0] - 1
        width = coordinate[1]

        while height >= 0:
            for x in range(width):
                grid[height][x] += 1
            height -= 1

    for row in grid:
        print row



coordinates = [(2, 3), (1, 7), (4, 5)]

highest_overlapping_areas(coordinates)