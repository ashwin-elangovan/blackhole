def lcs(X, Y):
  memo = {}

  def lcs_helper(i, j):
    if i == 0 or j == 0:
      return 0

    if (i, j) not in memo:
      if X[i - 1] == Y[j - 1]:
        memo[(i, j)] = 1 + lcs_helper(i - 1, j - 1)
      else:
        memo[(i, j)] = max(lcs_helper(i - 1, j), lcs_helper(i, j - 1))

    return memo[(i, j)]

  return lcs_helper(len(X), len(Y))


X = "AGGTAB"
Y = "GXTXAYB"
result = lcs(X, Y)
print(result)


#######

def lcs(X, Y, i, j, memo):
  if i == 0 or j == 0:
      return 0

  if (i, j) not in memo:
      if X[i - 1] == Y[j - 1]:
          memo[(i, j)] = 1 + lcs(X, Y, i - 1, j - 1, memo)
      else:
          memo[(i, j)] = max(lcs(X, Y, i - 1, j, memo), lcs(X, Y, i, j - 1, memo))

  return memo[(i, j)]

X = "AGGTAB"
Y = "GXTXAYB"
memo = {}
result = lcs(X, Y, len(X), len(Y), memo)
print(result)