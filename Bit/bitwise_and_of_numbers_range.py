class Solution:

  def rangeBitwiseAnd(self, left: int, right: int) -> int:
    # If left and right are equal, the result will be either left or right.
    if left == right:
      return left & right

    # If right is at least twice greater than left, the result will be 0.
    if right >= 2 * left:
      return 0

    # Initialize the result with the value of left.
    result = left

    # Iterate through the range from left+1 to right (inclusive).
    for num in range(left + 1, right + 1):
      # Perform bitwise AND operation between the result and the current number.
      result = result & num

    # Return the final result.
    return result
