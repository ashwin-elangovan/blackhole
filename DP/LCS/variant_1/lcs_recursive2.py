class Solution:
  def longestCommonSubsequence(self, s1: str, s2: str) -> int:
      return self.lcs_recursive(s1, s2, len(s1), len(s2), {})

  def lcs_recursive(self, s1: str, s2: str, m: int, n: int, memo: dict) -> int:
      if m == 0 or n == 0:
          return 0

      if (m, n) in memo:
          return memo[(m, n)]

      if s1[m-1] == s2[n-1]:
          result = 1 + self.lcs_recursive(s1, s2, m-1, n-1, memo)
      else:
          take = self.lcs_recursive(s1, s2, m-1, n-1, memo)
          not_take1 = self.lcs_recursive(s1, s2, m, n-1, memo)
          not_take2 = self.lcs_recursive(s1, s2, m-1, n, memo)
          result = max(take, not_take1, not_take2)

      memo[(m, n)] = result
      return result