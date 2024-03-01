# if i=0 or j=0, then OPT(i,j)=0.
# Otherwise, OPT(i,j)=max(OPT(i−1,j),OPT(i,j−1),OPT(i−1,j−1)+1)

def lcs(X, Y):
  m, n = len(X), len(Y)
  
  # Initialize a 2D array to store the results of subproblems
  dp = [[0] * (n + 1) for _ in range(m + 1)]
  
  # Helper function to calculate the match score
  def match_score(i, j):
      return 1 if X[i - 1] == Y[j - 1] else 0
  
  # Fill in the dp array using the recurrence relation
  for i in range(1, m + 1):
      for j in range(1, n + 1):
          dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + match_score(i, j))
  
  return dp[m][n]

X = "AGGTAB"
Y = "GXTXAYB"
result = lcs(X, Y)
print(result)


#######

class Solution:
  def longestCommonSubsequence(self, X, Y):
      m, n = len(X), len(Y)

      # Initialize a 2D array to store the results of subproblems
      dp = [[0] * (n + 1) for _ in range(m + 1)]

      # Helper function to calculate the match score
      def match_score(i, j):
          return 1 if X[i - 1] == Y[j - 1] else 0

      # Fill in the dp array using the recurrence relation
      for i in range(1, m + 1):
          for j in range(1, n + 1):
              dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + match_score(i, j))

      return dp[m][n]

# Example usage:
sol = Solution()
X = "AGGTAB"
Y = "GXTXAYB"
result = sol.longestCommonSubsequence(X, Y)
print(result)
