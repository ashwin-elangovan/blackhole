class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
      # Get the number of rows and columns in the grid
      row_len = len(obstacleGrid)
      col_len = len(obstacleGrid[0])

      # Create a 2D array (dp) to store the number of unique paths to reach each cell
      # Initialize all cells to 0
      dp = [[0 for _ in range(col_len+1)] for _ in range(row_len+1)]

      # Initialize the starting cell (0, 1) with 1 as there's only one way to reach it
      dp[0][1] = 1

      # Iterate through each cell in the grid
      for i in range(1, row_len+1):
          for j in range(1, col_len+1):
              # If the current cell is an obstacle, set the number of paths to 0
              if obstacleGrid[i-1][j-1] == 1:
                  dp[i][j] = 0
              else:
                  # Otherwise, calculate the number of unique paths to reach the current cell
                  # It's the sum of paths from the cell above (i-1, j) and the cell to the left (i, j-1)
                  dp[i][j] = dp[i-1][j] + dp[i][j-1]

      # Return the number of unique paths to reach the bottom-right cell of the grid
      return dp[row_len][col_len]
