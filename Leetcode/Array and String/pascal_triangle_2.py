# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Input: rowIndex = 3
# Output: [1,3,3,1]

# Say we have the current layer [1, 2, 1]. We then make 2 copies of this layer, add 0 to the start of one copy, and add 0 to the end of one copy; then we have [0, 1, 2, 1] and [1, 2, 1, 0]. Then we can perform the element-wise add operation and we would have [1, 3, 3, 1]. This is from the definition of Pascal's Triangle.

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1] # Initialize first row
        for _ in range(rowIndex): # Until given row loop will run. for _ in range is a pythonic way to run loop without variable declaration.
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row


# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")

# x = zip(a, b)
# (('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))


