class Solution:

  def splitArray(self, nums: List[int], k: int) -> int:
    # Initialize search range
    l = max(nums)  # Lower bound
    r = sum(nums)  # Upper bound

    # Helper function to check if mid is a feasible solution
    def feasible(mid):
      curr_count = 1  # Initialize count of subarrays
      tempCount = mid  # Initialize temporary count
      # Iterate through nums to check if mid is feasible
      for num in nums:
        if tempCount - num < 0:  # If current subarray exceeds mid
          curr_count += 1  # Increment count of subarrays
          tempCount = mid  # Reset temporary count
        tempCount -= num  # Update temporary count
      return curr_count <= k  # Return True if curr_count <= k

    # Binary search to find the minimum feasible value
    while l < r:
      mid = l + (r - l) // 2  # Calculate mid
      if feasible(mid):  # If mid is feasible
        r = mid  # Update upper bound
      else:
        l = mid + 1  # Update lower bound
    return l  # Return the minimum feasible value
