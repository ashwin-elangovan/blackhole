def lcs(X, Y):
  m, n = len(X), len(Y)

  # Create a 2D table to store the lengths of LCS
  dp = [[""] * (n + 1) for _ in range(m + 1)]

  # Build the LCS table
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if X[i - 1] == Y[j - 1]:
        dp[i][j] = dp[i - 1][j - 1] + X[i - 1]  # Concatenate the character
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
  print(dp)
  return dp[m][n]  # Return the LCS string


# Example usage:
X = "ABCBDAB"
Y = "BDCAB"
result = lcs(X, Y)
print("Longest Common Subsequence:", result)

########


def lcs_recursive(X, Y, m, n):
  # Base case: if either of the sequences is empty
  if m == 0 or n == 0:
    return ""

  # If the last characters match
  if X[m - 1] == Y[n - 1]:
    return lcs_recursive(X, Y, m - 1, n - 1) + X[m - 1]

  # If the last characters do not match
  lcs1 = lcs_recursive(X, Y, m - 1, n)
  lcs2 = lcs_recursive(X, Y, m, n - 1)

  # Return the longer of the two LCS strings
  if len(lcs1) > len(lcs2):
    return lcs1
  else:
    return lcs2


# Example usage:
X = "ABCBDAB"
Y = "BDCAB"
result = lcs_recursive(X, Y, len(X), len(Y))
print("Longest Common Subsequence:", result)
