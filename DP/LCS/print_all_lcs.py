def print_all_lcs(X, Y, m, n, memo):
  if m == 0 or n == 0:
    return [""]

  if (m, n) in memo:
    return memo[(m, n)]

  if X[m - 1] == Y[n - 1]:
    lcs_list = [
      seq + X[m - 1] for seq in print_all_lcs(X, Y, m - 1, n - 1, memo)
    ]
  else:
    lcs_list = []
    lcs_list.extend(print_all_lcs(X, Y, m - 1, n, memo))
    lcs_list.extend(print_all_lcs(X, Y, m, n - 1, memo))

  memo[(m, n)] = lcs_list
  return lcs_list


def get_all_lcs(X, Y):
  m, n = len(X), len(Y)
  memo = dict()
  lcs_list = print_all_lcs(X, Y, m, n, memo)
  return lcs_list


# Example usage:
X = "ABCBDAB"
Y = "BDCAB"
result = get_all_lcs(X, Y)
print("All Longest Common Subsequences:", result)
