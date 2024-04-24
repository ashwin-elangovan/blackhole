class Solution:

  def maxProfit(self, prices: List[int]) -> int:
    # Initialize the maximum profit to 0
    max_profit = 0

    # Initialize the smallest element encountered so far to positive infinity
    smallest_element = float('inf')

    # Iterate through the prices
    for idx in range(len(prices)):
      # Update the smallest element if the current price is smaller
      if prices[idx] < smallest_element:
        smallest_element = prices[idx]
      else:
        # Calculate the current profit if selling at the current price
        curr_profit = prices[idx] - smallest_element

        # Update the maximum profit if the current profit is greater
        max_profit = max(max_profit, curr_profit)

    # Return the maximum profit
    return max_profit
