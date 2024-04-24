class Solution(object):

  def maxProfit(self, prices):
    # Initialize variables to track the maximum profit at each step
    # T_ik0 represents the maximum profit when we do not hold any stock at step i
    # T_ik1 represents the maximum profit when we hold one stock at step i
    T_ik0 = 0  # Maximum profit without holding any stock initially
    T_ik1 = float(
      '-inf'
    )  # Maximum profit with one stock initially (initialized to negative infinity)

    # Iterate through each price in the prices list
    for price in prices:
      # Keep track of the previous value of T_ik0 for updating T_ik1
      T_ik0_old = T_ik0

      # Update T_ik0: maximum of current T_ik0 and T_ik1 + current price (selling the stock)
      T_ik0 = max(T_ik0, T_ik1 + price)

      # Update T_ik1: maximum of current T_ik1 and previous T_ik0 - current price (buying the stock)
      T_ik1 = max(T_ik1, T_ik0_old - price)

    # Return the maximum profit without holding any stock at the end
    return T_ik0
