class Solution:
    def spiralOrder(self, matrix):
        if matrix: # pop will modify original array
            # zip(*matrix) will transpose it and [::-1] will reverse it
            return [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
        else:
            return matrix
        # return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

# So the last line in your code:

# return username and USER_RE.match(username)
# is the same as:

# if username:
#     return USER_RE.match(username)
# else:
#     return username


# <!-- Visualization
# Here's how the matrix changes by always extracting the first row and rotating the remaining matrix counter-clockwise:

#     |1 2 3|      |6 9|      |8 7|      |4|  =>  |5|  =>  ||
#     |4 5 6|  =>  |5 8|  =>  |5 4|  =>  |5|
#     |7 8 9|      |4 7|
# Now look at the first rows we extracted:

#     |1 2 3|      |6 9|      |8 7|      |4|      |5|
# Those concatenated are the desired result.

# Another visualization
#   spiral_order([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])

# = [1, 2, 3] + spiral_order([[6, 9],
#                             [5, 8],
#                             [4, 7]])

# = [1, 2, 3] + [6, 9] + spiral_order([[8, 7],
#                                      [5, 4]])

# = [1, 2, 3] + [6, 9] + [8, 7] + spiral_order([[4],
#                                               [5]])

# = [1, 2, 3] + [6, 9] + [8, 7] + [4] + spiral_order([[5]])

# = [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + spiral_order([])

# = [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + []

# = [1, 2, 3, 6, 9, 8, 7, 4, 5] -->