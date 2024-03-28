from collections import defaultdict

class Solution:

  def maxSubarrayLength(self, nums: List[int], k: int) -> int:
    # Initialize left and right pointers, current count dictionary, and maximum count
    left, right = 0, 0
    curr_count = defaultdict(
      lambda: 0)  # Dictionary to store current count of elements
    max_count = 0  # Variable to store the maximum count of subarrays satisfying the condition

    # Iterate through the array using the sliding window technique
    while right < len(nums):
      # Increment the count of the current element
      curr_count[nums[right]] += 1

      # Shrink the window from the left until the count of all elements satisfies the condition
      while curr_count[nums[right]] > k:
        curr_count[nums[
          left]] -= 1  # Decrement the count of the element at the left pointer
        left += 1  # Move the left pointer forward

      # Update the maximum count by comparing with the length of the current subarray
      max_count = max(max_count, right - left + 1)

      # Move the right pointer forward to expand the window
      right += 1

    # Return the maximum count of subarrays satisfying the condition
    return max_count
