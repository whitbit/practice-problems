print 'BEFORE'
grid = [[0 for i in range(4)]for i in range(4)]
grid[1][1] = 1
grid[3][2] = 1
for row in grid:
    print row
print '**************'

def find_coordinates(matrix):
    all_coordinates = []

    row_length = len(matrix[0])
    col_length = len(matrix)

    for row in range(row_length):
        for col in range(col_length):
            if matrix[row][col] == 1:
                all_coordinates.append((row, col))

    return all_coordinates

def update_columns(matrix):
    
    coordinates = find_coordinates(matrix)
    
    row_length = len(matrix[0])
    col_length = len(matrix)

    for coordinate in coordinates:
        row, col = coordinate

        for i in range(row_length):
            grid[row][i] = 1
        for j in range(col_length):
            grid[j][col] = 1

print 'AFTER'
update_columns(grid)
for row in grid:
    print row
