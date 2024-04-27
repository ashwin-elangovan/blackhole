from typing import List


class Solution:

  def minPathSum(self, grid: List[List[int]]) -> int:
    # Get the number of rows and columns in the grid
    row_len = len(grid)
    col_len = len(grid[0])

    # Initialize a 2D array to store the minimum path sum values
    dp = [[0 for _ in range(col_len)] for _ in range(row_len)]

    # Calculate the minimum path sum values for the first column
    curr_val = 0
    for idx in range(row_len):
      curr_val += grid[idx][0]
      dp[idx][0] = curr_val

    # Calculate the minimum path sum values for the first row
    curr_val = 0
    for idx in range(col_len):
      curr_val += grid[0][idx]
      dp[0][idx] = curr_val

    # Calculate the minimum path sum values for the rest of the grid
    for row_idx in range(1, row_len):
      for col_idx in range(1, col_len):
        # Choose the minimum of the top and left cells and add the current cell value
        dp[row_idx][col_idx] = min(
          dp[row_idx - 1][col_idx],
          dp[row_idx][col_idx - 1]) + grid[row_idx][col_idx]

    # Return the minimum path sum value for the bottom-right cell
    return dp[row_len - 1][col_len - 1]
