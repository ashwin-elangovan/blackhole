class Solution(object):

  def maxProfit(self, k, prices):
    # No transaction, No profit
    if k == 0:
      return 0

    # dp[k][0] = min cost you need to spend at most k transactions
    # dp[k][1] = max profit you can achieve at most k transactions

    dp = [[float('inf'), 0] for _ in range(k + 1)]

    # It calculates the minimum cost (dp[i][0]) and maximum profit (dp[i][1]) for the current transaction count i.
    for price in prices:
      for i in range(1, k + 1):
        # dp[i][0]: Represents the minimum amount of money needed to complete i transactions.
        # It is updated by taking the minimum between the current dp[i][0] and the difference between the current price and the profit earned from the previous transaction (price - dp[i - 1][1]).
        # Using earlier profit, we'll get the minimum amount of money needed
        dp[i][0] = min(dp[i][0], price - dp[i - 1][1])
        # dp[i][1]: Represents the maximum profit achievable after completing i transactions.
        # It is updated by taking the maximum between the current dp[i][1] and the difference between the current price and the minimum cost achieved in the previous step (price - dp[i][0]).
        # Using minimum amount of money we have, we'll reduce it with the price to improve the profit.
        dp[i][1] = max(dp[i][1], price - dp[i][0])
    return dp[-1][1]
