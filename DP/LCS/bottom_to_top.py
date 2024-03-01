class Solution:
  def longestCommonSubsequence(self, X, Y):
      m, n = len(X), len(Y)

      # Memoization cache
      memo = dict()

      # Helper function for recursive calls with memoization
      def lcs_recursive(i, j):
          if i == m or j == n:
              return 0

          if (i, j) in memo:
              return memo[(i, j)]

          if X[i] == Y[j]:
              result = 1 + lcs_recursive(i + 1, j + 1)
          else:
              result = max(lcs_recursive(i, j + 1), lcs_recursive(i + 1, j))

          memo[(i, j)] = result
          return result

      # Start the recursive calls from the top-left corner
      return lcs_recursive(0, 0)

# Example usage:
sol = Solution()
X = "pmjghexybyrgzczy"
Y = "hafcdqbgncrcbihkd"
result = sol.longestCommonSubsequence(X, Y)
print(result)
