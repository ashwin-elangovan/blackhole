class Solution:

  def minFallingPathSum(self, A: List[List[int]]) -> int:
    # Get the number of rows and columns in the input matrix A
    n, m = len(A), len(A[0])

    # Initialize a DP array with each element initialized to positive infinity,
    # and add additional columns at the beginning and end filled with positive infinity
    dp = [[float('inf')] + A[i] + [float('inf')] for i in range(n)]

    # Iterate over rows starting from the second row
    for i in range(1, n):
      # Iterate over columns
      for j in range(1, m + 1):
        # Calculate the minimum falling path sum for the current cell
        # by adding the current cell value with the minimum of the three neighboring cells
        dp[i][j] = dp[i][j] + min(dp[i - 1][j - 1], dp[i - 1][j],
                                  dp[i - 1][j + 1])

    # Return the minimum falling path sum from the last row of the DP array
    return min(dp[-1])
