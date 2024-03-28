class Solution:

  def kthSmallest(self, matrix, k):
    # Define a function to check if there are at least k elements smaller than or equal to the given threshold 'mid'
    def feasible(mid):
      count = 0  # Initialize a counter for elements smaller than or equal to 'mid'
      col_idx = len(
        matrix[0]) - 1  # Start from the rightmost column of the matrix
      # Iterate over each row of the matrix
      for r in range(len(matrix)):
        # Iterate over the columns from right to left until the value is greater than 'mid'
        while col_idx >= 0 and matrix[r][col_idx] > mid:
          col_idx -= 1
        # Increment the count by the number of elements found in the current row
        count += (col_idx + 1)
      # Check if the count of elements is greater than or equal to 'k'
      return count >= k

    # Initialize the search range using the smallest and largest elements in the matrix
    left, right = matrix[0][0], matrix[-1][-1]
    # Perform binary search to find the kth smallest element
    while left < right:
      mid = left + (right - left) // 2  # Calculate the mid value
      # If there are at least k elements smaller than or equal to 'mid', move the right pointer
      if feasible(mid):
        right = mid
      # Otherwise, move the left pointer
      else:
        left = mid + 1
    # Return the left pointer value, which represents the kth smallest element
    return left
