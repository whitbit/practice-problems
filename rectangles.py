# w, h = 5, 5;
# Matrix = [[0 for x in range(w)] for y in range(h)] 

# Matrix[0][4] = 1
# # Matrix[1][3] = 1
# Matrix[1][2] = 1
# Matrix[1][1] = 1
# Matrix[2][2] = 1
# Matrix[2][1] = 1
# Matrix[3][1] = 1

# Matrix[3][2] = 1




# for line in Matrix:
#     print line

# # https://leetcode.com/problems/maximal-rectangle/discuss/29065

# # def maximalRectangle(self, matrix):
# #     if not matrix or not matrix[0]:
# #         return 0
# #     n = len(matrix[0])
# #     height = [0] * (n + 1)
# #     ans = 0
# #     for row in matrix:
# #         for i in xrange(n):
# #             height[i] = height[i] + 1 if row[i] == '1' else 0
# #         stack = [-1]
# #         for i in xrange(n + 1):
# #             while height[i] < height[stack[-1]]:
# #                 h = height[stack.pop()]
# #                 w = i - 1 - stack[-1]
# #                 ans = max(ans, h * w)
# #             stack.append(i)
# #     return ans

# def is_rectangle(matrix):

#     row_length = len(matrix[0])
#     column_length = len(matrix)

#     for y in range(column_length - 1):
#         for x in range(row_length - 1):
#             if(matrix[y][x] == 1
#               and matrix[y][x+1] == 1
#               and matrix[y+1][x+1] == 1
#               and matrix[y+1][x] == 1):
#               return (y, x)
#     raise Exception('No Rectangle!')

# coordinates = is_rectangle(Matrix)
# print coordinates

# def find_width_and_height(x_lc, y_lc, matrix):

#     row_length = len(matrix[0])
#     column_length = len(matrix)

#     width = 0
#     height = 0

#     for x in range(x_lc, row_length):
#         if matrix[y_lc][x] == 1:
#             width += 1

#     for y in range(y_lc, column_length):
#         if matrix[y][x_lc] == 1:
#             height += 1

#     print (width, height)

# find_width_and_height(coordinates[0], coordinates[1], Matrix)


# def bubble_sort(ints):

#     for i in range(len(ints)):
#         print i
#         for j in range(0, len(ints)-i-1):
#             if ints[j] > ints[j+1]:
#                 ints[j], ints[j+1] = ints[j+1], ints[j]

# nums = [3,5,7,1,4,7]
# bubble_sort(nums)
# print nums


def has_rectangle(matrix):
    
    for y in len(matrix):
        for x in len(matrix):
            if(matrix[y][x] == 1
               and matrix[y][x+1] == 1):
                return True
            if(matrix[y][x] == 1
               and matrix[y+1][x] == 1):
                return True
    return False

row, height = 5, 5

grid = [[0] * row] * height
# print grid
for row in grid:
    print row
