class Solution:

  def shipWithinDays(self, weights: List[int], days: int) -> int:
    # Initialize the search range
    low, high = max(weights), sum(weights)
    # Initialize the result to the maximum possible value
    # res = high

    # Define a helper function to check if the given capacity satisfies the conditions
    def feasible(capacity):
      tempDays = 1
      tempCapacity = capacity
      for weight in weights:
        if tempCapacity - weight < 0:
          tempDays += 1
          tempCapacity = capacity
        tempCapacity -= weight
      # Return True if the capacity can ship all weights within the given days
      return tempDays <= days

    # Perform binary search to find the minimum capacity that satisfies the conditions
    while low < high:
      mid = (low + high) // 2
      if feasible(mid):
        # Update the result and narrow down the search range
        # res = min(res, mid)
        high = mid
      else:
        # Adjust the search range
        low = mid + 1
    # Return the minimum capacity that satisfies the conditions
    return low
