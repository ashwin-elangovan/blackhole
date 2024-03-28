class Solution:

  def mySqrt(self, x: int) -> int:
    # Base cases: if x is 0 or 1, return x
    if x == 0 or x == 1:
      return x

    # Initialize the left and right boundaries for binary search
    left, right = 0, x

    # Binary search to find the square root
    while left < right:
      mid = left + (right - left) // 2
      # If square value is equal it'll become left +  which will be managed in the return statement left - 1 If not a proper square value, it'll be left -1 which will handle the floor functionality
      if mid * mid <= x:
        left = mid + 1
      else:
        right = mid

    # Return the floor value of the square root
    return left - 1
