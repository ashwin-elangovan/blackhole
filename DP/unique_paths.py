class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
      # Create a 2D array (dp) to store the number of unique paths to reach each cell
      # Initialize all cells to 0
      dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

      # Initialize the starting cell (1, 0) with 1 as there's only one way to reach it
      dp[1][0] = 1

      # Iterate through each cell in the grid
      for i in range(1, m+1):
          for j in range(1, n+1):
              # Calculate the number of unique paths to reach the current cell (i, j)
              # It's the sum of paths from the cell above (i-1, j) and the cell to the left (i, j-1)
              dp[i][j] = dp[i-1][j] + dp[i][j-1]

      # Return the number of unique paths to reach the bottom-right cell (m, n)
      return dp[m][n]
