class Solution(object):

  def maxProfit(self, prices, fee):
    # Initialize the profit variables
    T_ik0 = 0  # Profit without any stocks in hand
    T_ik1 = float('-inf')  # Profit with stocks in hand (initialized to negative infinity)

    # Iterate through the prices
    for price in prices:
      # Store the previous day's profit without stocks in hand
      T_ik0_1 = T_ik0

      # Update the profit without stocks in hand:
      # - Do not buy or sell on the current day (no change)
      # - Sell the stock bought previously
      T_ik0 = max(T_ik0, T_ik1 + price)

      # Update the profit with stocks in hand:
      # - Do not buy or sell on the current day (no change)
      # - Buy a stock (subtracting fee) if it results in higher profit
      T_ik1 = max(T_ik1, T_ik0_1 - price - fee)

    # Return the maximum profit without any stocks in hand
    return T_ik0
