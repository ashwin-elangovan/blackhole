class Solution:

  def minFallingPathSum(self, grid: List[List[int]]) -> int:
    # Copy the grid to the dp array to store the minimum falling path sum
    dp = [row[:] for row in grid]

    # Initialize the min_row variable with the first row of the grid
    min_row = dp[0]

    # Iterate over each row starting from the second row
    for row in range(1, len(grid)):
      # Find the index of the smallest and second smallest values in the min_row
      smallest_val_idx = min_row.index(min(min_row))
      second_smallest_idx = min_row.index(
        min(min_row[:smallest_val_idx] + min_row[smallest_val_idx + 1:]))

      # Iterate over each column in the current row
      for col in range(len(grid[0])):
        # Update the value in the dp array by adding the value from the current row
        # and the smallest or second smallest value from the previous row
        if col != smallest_val_idx:
          dp[row][col] += min_row[smallest_val_idx]
        else:
          dp[row][col] += min_row[second_smallest_idx]

        # Alternative approach using commented-out code:
        # Calculate the minimum value from the previous row excluding the current column
        # min_val = float('inf')
        # for idx in range(len(grid[row-1])):
        #     if col != idx:
        #         min_val = min(min_val, grid[row-1][idx])
        # Add the minimum value to the current value in the dp array
        # dp[row][col] += min_val

      # Update min_row for the next iteration
      min_row = dp[row]

    # Return the minimum falling path sum from the last row of the dp array
    return min(dp[-1])
