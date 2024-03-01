def lcs(X, Y):
  # Helper function for recursive calls
  def lcs_helper(i, j):
    if i == 0 or j == 0:
      return 0

    match_score = 1 if X[i - 1] == Y[j - 1] else 0

    return max(lcs_helper(i - 1, j), lcs_helper(i, j - 1),
               lcs_helper(i - 1, j - 1) + match_score)

  # Start the recursive calls from the end of the strings
  return lcs_helper(len(X), len(Y))


# Example usage:
X = "AGGTAB"
Y = "GXTXAYB"
result = lcs(X, Y)
print(result)

#######

class Solution:
  def longestCommonSubsequence(self, X, Y):
      # Helper function for recursive calls
      def lcs_helper(i, j):
          if i == 0 or j == 0:
              return 0

          match_score = 1 if X[i - 1] == Y[j - 1] else 0

          return max(lcs_helper(i - 1, j), lcs_helper(i, j - 1),
                     lcs_helper(i - 1, j - 1) + match_score)

      # Start the recursive calls from the end of the strings
      return lcs_helper(len(X), len(Y))

# Example usage:
sol = Solution()
X = "AGGTAB"
Y = "GXTXAYB"
result = sol.longestCommonSubsequence(X, Y)
print(result)
