class Solution:

  def findKthLargest(self, nums: List[int], k: int) -> int:

    def feasible(mid):
      """
          Determine whether there are at least k elements greater than mid in the nums array.

          Args:
          - mid: The threshold value to compare elements against.

          Returns:
          - bool: True if there are at least k elements greater than mid, False otherwise.
          """
      count = 0
      for num in nums:
        if num > mid:
          count += 1
      return count >= k

    left, right = min(nums), max(
      nums
    )  # Initialize left and right pointers to the minimum and maximum values in nums
    while left < right:
      mid = left + (right - left) // 2  # Calculate the middle value
      if feasible(mid):  # If there are at least k elements greater than mid
        left = mid + 1  # Update the left pointer to mid + 1
      else:
        right = mid  # Otherwise, update the right pointer to mid
    return left  # Return the kth largest element found
