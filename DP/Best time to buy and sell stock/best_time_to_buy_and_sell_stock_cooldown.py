class Solution(object):
  def maxProfit(self, prices):
      # Profit from 2 days earlier
      T_ik0_2 = 0

      # Profit at the end of the day
      T_ik0 = 0

      # Initially no way to have stock without any transaction
      T_ik1 = float('-inf')

      for price in prices:
          # Set previous day's profit to 1 day earlier variable
          T_ik0_1 = T_ik0

          # Calculate the maximum profit if we don't hold any stock at the end of the day
          # T_ik1 represents previous day's k transaction's buy (T[i-1][k][1])
          T_ik0 = max(T_ik0, T_ik1 + price)

          # Calculate the maximum profit if we hold a stock at the end of the day
          # Use the profit from 2 days earlier to ensure a cooldown period
          # T_ik0_2 T[i-2][k-1][0]
          T_ik1 = max(T_ik1, T_ik0_2 - price)

          # Update the profit from 2 days earlier for the next iteration
          T_ik0_2 = T_ik0_1

      return T_ik0
