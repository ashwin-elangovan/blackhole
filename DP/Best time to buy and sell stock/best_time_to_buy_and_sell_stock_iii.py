class Solution:

  def maxProfit(self, prices: List[int]) -> int:
    # Initialize variables for the three states of transactions:
    # T_i00: Represents no transaction at all.
    # T_i10: Represents the first transaction done.
    # T_i11: Represents the first transaction in progress.
    # T_i20: Represents the second transaction done.
    # T_i21: Represents the second transaction in progress.
    T_i00 = 0  # No transaction done initially

    T_i10 = 0  # First transaction done, profit is zero
    T_i11 = float(
      '-inf'
    )  # First transaction in progress, initially set to negative infinity

    T_i20 = 0  # Second transaction done, profit is zero
    T_i21 = float(
      '-inf'
    )  # Second transaction in progress, initially set to negative infinity

    # Iterate through each price in the prices list
    for price in prices:
      # Update T_i20 and T_i21 based on the current price
      T_i20 = max(T_i20, T_i21 + price)
      T_i21 = max(T_i21, T_i10 - price)

      # Update T_i10 and T_i11 based on the current price
      T_i10 = max(T_i10, T_i11 + price)
      T_i11 = max(T_i11, T_i00 - price)

    # The final profit after the second transaction is complete is stored in T_i20
    return T_i20
