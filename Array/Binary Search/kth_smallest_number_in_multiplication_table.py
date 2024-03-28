class Solution:

  def findKthNumber(self, row: int, col: int, k: int) -> int:
    # Define a function to check if enough numbers are present up to a given mid value
    def enough(mid_value) -> bool:
      count = 0
      # Iterate through each row
      for current_row in range(1, row + 1):  # count row by row
        # Calculate the number of values that can be accommodated in the current row
        curr_row_values_count = min(mid_value // current_row, col)
        # If no values can be accommodated in the current row, stop counting
        if curr_row_values_count == 0:
          break
        count += curr_row_values_count
      # Check if the total count of values is at least k
      return count >= k

    # Initialize binary search boundaries
    left, right = 1, row * col

    # Perform binary search to find the kth number
    while left < right:
      mid = left + (right - left) // 2
      # If enough values are present up to the current mid value, move to the left half
      if enough(mid):
        right = mid
      # If not enough values are present, move to the right half
      else:
        left = mid + 1
    # Return the left boundary as the kth number
    return left
